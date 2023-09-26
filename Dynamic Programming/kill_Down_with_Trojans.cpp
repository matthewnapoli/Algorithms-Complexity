#include <iostream>
#include <fstream>
#include <vector>
#include <cstring> // For strlen

constexpr int MAX_N = 100;

struct Tile {
    int t;
    int v;
};

void load_input_file(const std::string& file_name, int& n, int& H, std::vector<std::vector<Tile>>& tiles) {
    std::ifstream file(file_name);
    file >> n >> H;
    
    // Initialize the grid
    tiles.resize(n, std::vector<Tile>(n));

    for (int i = 0; i < n * n; i++) {
        if (i == 0) {
            continue; // The initial tile is zero type with zero value
        }
        Tile tile;
        int x,y;
        file >> x >> y >> tile.t >> tile.v;
        tiles[x][y] = tile;
    }
    
    file.close();
}

void print_tile_data(int n, const std::vector<std::vector<Tile>>& tiles) {
    std::cout << "Tile Types:\n";
    for (int x = 0; x < n; x++) {
        for (int y = 0; y < n; y++) {
            std::cout << "[" << tiles[x][y].t << "] ";
        }
        std::cout << '\n';
    }

    std::cout << "\nTile Values:\n";
    for (int x = 0; x < n; x++) {
        for (int y = 0; y < n; y++) {
            std::cout << "[" << tiles[x][y].v << "] ";
        }
        std::cout << '\n';
    }
}

bool DP(int n, int H, const std::vector<std::vector<Tile>>& tiles) {
    // TODO
    // Placeholder function - implement your logic here
    // Your code to check whether it is possible to reach the bottom-right
    // corner without running out of HP should go here.
    // You should use dynamic programming to solve the problem.
    // Return true if possible, false otherwise.
    
    // By default, we return false
    // TODO you should change this
    bool res = false;
    return res;
}

void write_output_file(const std::string& output_file_name, bool result) {
    std::ofstream file(output_file_name);
    file << result;
    file.close();
}

int main(int argc, char* argv[]) {
    if (argc != 2) {
        std::cout << "Usage: " << argv[0] << " a_file_name.txt\n";
        return 1;
    }

    int n, H;
    std::vector<std::vector<Tile>> tiles;
    load_input_file(argv[1], n, H, tiles);
    print_tile_data(n, tiles);
    bool result = DP(n, H, tiles);
    std::cout << "Result: " << result << '\n';
    
    // Construct the output file name
    std::string output_file_name(argv[1]);
    output_file_name.insert(output_file_name.find_last_of('.'), "_out");
    std::ofstream outfile(output_file_name);
    outfile << result;
    outfile.close();

    return 0;
}
