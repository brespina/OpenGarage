#include <iostream>
#include <fstream>
#include <string>
#include <pthread.h>
#include <unistd.h>
#include <vector>
#include <chrono>

struct threadData {
    std::string inputStr;
    std::string rleStr;
    std::vector<int> rleFreq;
    std::chrono::time_point<std::chrono::high_resolution_clock> startTime, endTime;
};

void* rle_encode(void* ptr) {
    threadData* rleData = (struct threadData*) ptr;  // Cast the void pointer to threadData*

    rleData->startTime = std::chrono::high_resolution_clock::now();
    std::string str = rleData->inputStr;
    std::string rle;
    std::vector<int> freq;
    int count;

    for (size_t i = 0; i < str.length(); ++i) {
        count = 1;
        while (i + 1 < str.length() && str[i] == str[i + 1]) {
            ++count;
            ++i;
        }
        if (count > 1) {
            rle += str[i];
            rle += str[i];
            freq.push_back(count);

            rle += "[";
            rle += std::to_string(count);
            rle += "]";
        } else {
            rle += str[i];
        }
    }

    rleData->rleStr = rle;
    rleData->rleFreq = freq;

    rleData->endTime = std::chrono::high_resolution_clock::now();
    return nullptr;
}

int main(int argc, char* argv[]) {
    if (argc != 2) {
        std::cerr << "Usage: " << argv[0] << " <input_file>" << std::endl;
        return 1;
    }

    std::ifstream inputFile(argv[1]);
    if (!inputFile.is_open()) {
        std::cerr << "Error: Could not open file " << argv[1] << std::endl;
        return 1;
    }

    std::vector<std::string> strVect;
    std::string line;

    while (std::getline(inputFile, line)) {
        if (!line.empty()) {
            strVect.push_back(line);
        }
    }
    inputFile.close();

    size_t numStrings = strVect.size();
    threadData* data = new threadData[numStrings];
    pthread_t* threads = new pthread_t[numStrings];

    for (size_t i = 0; i < numStrings; ++i) {
        data[i].inputStr = strVect[i];
        if (pthread_create(&threads[i], nullptr, rle_encode, &data[i])) {
            std::cerr << "Error: Could not create thread" << std::endl;
            delete[] data;
            delete[] threads;
            return 1;
        }
    }

    for (size_t i = 0; i < numStrings; ++i) {
        pthread_join(threads[i], nullptr);
    }

    for (size_t i = 0; i < numStrings; ++i) {
        std::cout << "Input string: " << data[i].inputStr << std::endl;
        std::cout << "RLE String: " << data[i].rleStr << std::endl;
        std::cout << "RLE Frequencies: ";
        for (int freq : data[i].rleFreq) {
            std::cout << freq << " ";
        }
        std::cout << std::endl;

        auto duration = std::chrono::duration_cast<std::chrono::milliseconds>(
                            data[i].endTime - data[i].startTime).count();
        std::cout << "Execution Time: " << duration << " ms" << std::endl;
        std::cout << "Memory Saved(in bytes): " << data[i].inputStr.size() - data[i].rleStr.size() << std::endl;
        std::cout << std::endl;
    }

    delete[] data;
    delete[] threads;
    return 0;
}
