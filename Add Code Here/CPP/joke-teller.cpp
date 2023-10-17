#include <iostream>
#include <vector>
#include <cstdlib>
#include <ctime>
#include <map>

int random(int min, int max) {
    return rand() % (max - min + 1) + min;
}

void printJoke(const std::string& joke) {
    std::cout << "Random Joke:\n" << joke << std::endl;
}

void addJoke(std::map<std::string, std::vector<std::string>>& jokeCategories, const std::string& category, const std::string& joke) {
    jokeCategories[category].push_back(joke);
    std::cout << "Joke added successfully!" << std::endl;
}

void removeJoke(std::map<std::string, std::vector<std::string>>& jokeCategories, const std::string& category, int index) {
    if (jokeCategories.find(category) != jokeCategories.end() && index >= 0 && index < jokeCategories[category].size()) {
        jokeCategories[category].erase(jokeCategories[category].begin() + index);
        std::cout << "Joke removed successfully!" << std::endl;
    } else {
        std::cout << "Invalid category or index. Try again." << std::endl;
    }
}

void printJokesByCategory(const std::map<std::string, std::vector<std::string>>& jokeCategories, const std::string& category) {
    if (jokeCategories.find(category) != jokeCategories.end()) {
        const std::vector<std::string>& jokes = jokeCategories.at(category);
        for (size_t i = 0; i < jokes.size(); ++i) {
            std::cout << i << ". " << jokes[i] << std::endl;
        }
    } else {
        std::cout << "Category not found. Try again." << std::endl;
    }
}

void listCategories(const std::map<std::string, std::vector<std::string>>& jokeCategories) {
    std::cout << "Available Categories:\n";
    for (const auto& category : jokeCategories) {
        std::cout << "- " << category.first << std::endl;
    }
}

void editJoke(std::map<std::string, std::vector<std::string>>& jokeCategories, const std::string& category, int index, const std::string& newJoke) {
    if (jokeCategories.find(category) != jokeCategories.end() && index >= 0 && index < jokeCategories[category].size()) {
        jokeCategories[category][index] = newJoke;
        std::cout << "Joke edited successfully!" << std::endl;
    } else {
        std::cout << "Invalid category or index. Try again." << std::endl;
    }
}

void clearAllJokes(std::map<std::string, std::vector<std::string>>& jokeCategories, const std::string& category) {
    if (jokeCategories.find(category) != jokeCategories.end()) {
        jokeCategories[category].clear();
        std::cout << "All jokes in category cleared successfully!" << std::endl;
    } else {
        std::cout << "Category not found. Try again." << std::endl;
    }
}

void viewAllJokes(const std::map<std::string, std::vector<std::string>>& jokeCategories) {
    for (const auto& category : jokeCategories) {
        std::cout << "Category: " << category.first << std::endl;
        for (const std::string& joke : category.second) {
            std::cout << "- " << joke << std::endl;
        }
    }
}

void viewRandomJokeByCategory(const std::map<std::string, std::vector<std::string>>& jokeCategories, const std::string& category) {
    if (jokeCategories.find(category) != jokeCategories.end() && !jokeCategories.at(category).empty()) {
        int randomIndex = random(0, jokeCategories.at(category).size() - 1);
        printJoke(jokeCategories.at(category)[randomIndex]);
    } else {
        std::cout << "Category not found or no jokes available. Try again." << std::endl;
    }
}

int main() {
    srand(time(0));

    std::map<std::string, std::vector<std::string>> jokeCategories;

    while (true) {
        std::cout << "\nOptions:\n"
                  << "1. Random Joke\n"
                  << "2. Add Your Own Joke\n"
                  << "3. Remove Joke\n"
                  << "4. View Jokes by Category\n"
                  << "5. List All Categories\n"
                  << "6. Edit Joke\n"
                  << "7. Clear All Jokes in Category\n"
                  << "8. View All Jokes\n"
                  << "9. View Random Joke by Category\n"
                  << "10. Quit\n";
        int choice;
        std::cin >> choice;
        std::cin.ignore(); // Clear newline from the input buffer

        if (choice == 1) {
            int randomCategoryIndex = random(0, jokeCategories.size() - 1);
            auto it = std::next(jokeCategories.begin(), randomCategoryIndex);
            int randomJokeIndex = random(0, it->second.size() - 1);
            printJoke(it->second[randomJokeIndex]);
        } else if (choice == 2) {
            std::string userCategory, userJoke;
            std::cout << "Enter the category: ";
            std::getline(std::cin, userCategory);
            std::cout << "Enter your joke: ";
            std::getline(std::cin, userJoke);
            addJoke(jokeCategories, userCategory, userJoke);
        } else if (choice == 3) {
            std::string userCategory;
            int index;
            std::cout << "Enter the category: ";
            std::getline(std::cin, userCategory);
            std::cout << "Enter the index of the joke to remove: ";
            std::cin >> index;
            removeJoke(jokeCategories, userCategory, index);
            std::cin.ignore(); // Clear newline from the input buffer
        } else if (choice == 4) {
            std::string userCategory;
            std::cout << "Enter the category: ";
            std::getline(std::cin, userCategory);
            printJokesByCategory(jokeCategories, userCategory);
        } else if (choice == 5) {
            listCategories(jokeCategories);
        } else if (choice == 6) {
            std::string userCategory, newJoke;
            int index;
            std::cout << "Enter the category: ";
            std::getline(std::cin, userCategory);
            std::cout << "Enter the index of the joke to edit: ";
            std::cin >> index;
            std::cin.ignore(); // Clear newline from the input buffer
            std::cout << "Enter the new joke: ";
            std::getline(std::cin, newJoke);
            editJoke(jokeCategories, userCategory, index, newJoke);
        } else if (choice == 7) {
            std::string userCategory;
            std::cout << "Enter the category: ";
            std::getline(std::cin, userCategory);
            clearAllJokes(jokeCategories, userCategory);
        } else if (choice == 8) {
            viewAllJokes(jokeCategories);
        } else if (choice == 9) {
            std::string userCategory;
            std::cout << "Enter the category: ";
            std::getline(std::cin, userCategory);
            viewRandomJokeByCategory(jokeCategories, userCategory);
        } else if (choice == 10) {
            break;
        } else {
            std::cout << "Invalid choice. Try again." << std::endl;
        }
    }

    return 0;
}
