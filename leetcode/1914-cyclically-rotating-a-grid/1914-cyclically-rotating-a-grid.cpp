class Solution {
public:
    vector<vector<int>> rotateGrid(vector<vector<int>>& grid, int k) {

        int rows = grid.size();
        int cols = grid[0].size();

        int layers = min(rows, cols) / 2; // number of layers

        for (int layer = 0; layer < layers; layer++) {

            vector<int> elements;

            int top = layer;
            int bottom = rows - layer - 1;
            int left = layer;
            int right = cols - layer - 1;

            for (int c = left; c <= right; c++) { // top row
                elements.push_back(grid[top][c]);
            }

            for (int r = top + 1; r < bottom; r++) { // right column
                elements.push_back(grid[r][right]);
            }

            for (int c = right; c >= left; c--) { // bottom row
                elements.push_back(grid[bottom][c]);
            }

            for (int r = bottom - 1; r > top; r--) { // left column
                elements.push_back(grid[r][left]);
            }

            int rotate = k % elements.size(); // avoid extra rotations

            vector<int> rotated;

            for (int i = rotate; i < elements.size(); i++) { // left part
                rotated.push_back(elements[i]);
            }

            for (int i = 0; i < rotate; i++) { // moved front part
                rotated.push_back(elements[i]);
            }

            int idx = 0;

            for (int c = left; c <= right; c++) { // put back top row
                grid[top][c] = rotated[idx++];
            }

            for (int r = top + 1; r < bottom; r++) { // put back right column
                grid[r][right] = rotated[idx++];
            }

            for (int c = right; c >= left; c--) { // put back bottom row
                grid[bottom][c] = rotated[idx++];
            }

            for (int r = bottom - 1; r > top; r--) { // put back left column
                grid[r][left] = rotated[idx++];
            }
        }

        return grid;
    }
};