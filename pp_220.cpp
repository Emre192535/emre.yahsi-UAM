/*
On the basis of Programming Task 03, additionally implement the functionality of writing the results to the file.
*/
#include <cctype>   // tolower
#include <cstddef>  // size_t
#include <fstream>
#include <iostream>
#include <regex>
#include <sstream>
#include <string>
#include <vector>

class Foo {
  public:
    /// @brief Load text file from disk as lines words to a private string; empty lines are NOT skipped.
    /// @param filepath Path to a text file (e.g., 'data/book.txt').
    Foo(const std::string &filepath, const std::size_t start_line = 0);

    /// @brief Return string containing all lines loaded from disk (as specified using 'start_line').
    /// @return String containing all lines.
    [[nodiscard]] inline const std::string &get_text() const { return s_text; }

    /// @brief Get (from cache) 5 letter words from text file.
    /// @return Vector containing 5 letter words (can be empty).
    const std::vector<std::string> &get_words();

  private:
    /// @brief String containing all lines loaded from disk.
    std::string s_text;
    /// @brief Vector containing all lines that match the regex pattern.
    std::vector<std::string> v_words_regex;

    /// @brief Return a vector of matches in `str` that were matched using `pattern`.
    /// @details This could be optimized further by modifying the `v_words_regex` directly; const cannot be used for `str`.
    /// @param pattern Regex pattern to use, e.g., `std::regex pattern(R"(\b\w{5}\b)")`.
    /// @param str String in which patterns will be found.
    /// @return Vector of individual matches.
    [[nodiscard]] std::vector<std::string> find_all(const std::regex &pattern, std::string &str) const;
};

/// @brief Ask user to provide a string to stdin; ask again if empty.
/// @param prompt Text to display before asking for input, e.g., `Enter the file to load: `.
/// @return String provided by user to stdin.
std::string get_input(const std::string &prompt);

/// @brief Convert string to size_t.
/// @param str String to be converted, e.g., `"20"`.
/// @return String as size_t, e.g., 20.
size_t str_to_size_t(const std::string &str);

int main()
{
    while (true) {
        const std::string filename = get_input("Enter filename: ");
        std::size_t u_start;
        while (true) {
            const std::string start = get_input("Enter line to start from: ");
            try {
                u_start = str_to_size_t(start);
            }
            catch (const std::runtime_error &e) {
                std::cout << "WARNING: " << e.what() << "\n";
                continue;
            }
            break;
        }
        std::cout << "DEBUG: filename=" << filename << "; u_start=" << u_start << '\n';
        // save to string so we can save it to file later
        std::string results;
        try {
            Foo f(filename, u_start);
            const std::vector<std::string> v_words = f.get_words();
            results += "Results:\n[";
            // crate python-style list printing
            for (const auto &word : v_words) {
                results += '\'' + word + "', ";
            }
            // results += "]\n" + "The amount of words is " + std::to_string(v_words.size()) + ".\n";
            results += "]\nThe amount of words is " + std::to_string(v_words.size()) + ".\n";
            std::cout << '\n'
                      << results;
        }
        catch (const std::runtime_error &e) {
            std::cout << "WARNING: " << e.what() << "\n";
            continue;
        }
        std::cout << "Write to file [yes/NO]: ";
        std::string prompt_bool;
        getline(std::cin, prompt_bool);
        // turn lowercase
        std::transform(prompt_bool.begin(), prompt_bool.end(), prompt_bool.begin(), ::tolower);
        const bool b_fwrite = (prompt_bool == "yes" || prompt_bool == "y") ? true : false;
        if (b_fwrite) {
            std::cout << "User requested writing to file.\n";
            const std::string filename_output = "output.txt";
            std::ofstream f(filename_output);
            if (!f) {
                std::cout << "WARNING: Failed to save results to file.\n";
                continue;
            }
            f << results;
            std::cout << "Results saved to: '" << filename_output << "'.\n";
        }
        else {
            std::cout << "User did not request writing to file, skipping.\n";
        }
    }
    return 0;
}

Foo::Foo(const std::string &filepath, const std::size_t start_line)
{
    std::ifstream f(filepath);
    if (!f) {
        throw std::runtime_error("File doesn't exist or can't be accessed.");
    }
    else {
        std::string line_buffer;
        std::size_t count = 0;
        while (std::getline(f, line_buffer)) {
            ++count;
            if (count < start_line) {
                // std::cout << "DEBUG: Skipping line, because below count (count=" << count << ").\n";
                continue;
            }
            else {
                this->s_text += line_buffer;
            }
        }
        s_text.shrink_to_fit();
        std::cout
            << "OK: Read '" << s_text.length() << "' characters.\n";
    }
}

[[nodiscard]] std::vector<std::string> Foo::find_all(const std::regex &pattern, std::string &str) const
{
    std::vector<std::string> res;
    std::regex_token_iterator<std::string::iterator> itr(str.begin(), str.end(), pattern);
    /// @brief Default constructor signals the end of the sequence.
    const std::regex_token_iterator<std::string::iterator> itr_end;
    while (itr != itr_end)
        res.push_back(*itr++);
    return res;
}

const std::vector<std::string> &Foo::get_words()
{
    // if not cached, process now, otherwise return from cache
    if (this->v_words_regex.empty()) {
        const std::regex pattern(R"(\b[aeoiuy]\w{3}[aeoiuy]\b)");
        // python-style re.findall(), storing all matches as items in vector
        this->v_words_regex = this->find_all(pattern, this->s_text);
        this->v_words_regex.shrink_to_fit();
    }
    return this->v_words_regex;
}

std::string get_input(const std::string &prompt)
{
    std::cout << prompt;
    std::string temp;
    while (true) {
        getline(std::cin, temp);
        if (temp.length() > 0) {
            break;
        }
        std::cout << "WARNING: no input provided.\n"
                  << prompt;
    }
    return temp;
}

size_t str_to_size_t(const std::string &str)
{
    size_t st;
    std::istringstream iss(str);
    iss >> st;
    if (iss.fail()) {
        throw std::runtime_error("Failed to convert '" + str + "' to size_t.");
    }
    return st;
}
