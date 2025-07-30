function numIslands(grid: string[][]): number {
    const rows = grid.length;
    const cols = grid[0].length;
    let count = 0;

    const bfs = (x,y) => {
        const queue = [];
        queue.push([x,y]);

        while(queue.length > 0) {
            const [r,c] = queue.shift();

            if(r < 0 || c < 0 || r >= rows || c >= cols || grid[r][c].toString() === '0') continue;

            grid[r][c] = '0';

            queue.push([r+1,c]);
            queue.push([r-1,c]);
            queue.push([r,c+1]);
            queue.push([r,c-1]);
        }
    }

    for(let i = 0; i < rows;i++){
        for( let  j = 0; j < cols ; j++){
            if(grid[i][j].toString() === '1'){
                bfs(i,j);
                count += 1;
            }
        }
    }

    return count;

};

