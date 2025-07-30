function maxAreaOfIsland(grid: number[][]): number {
    const rows = grid.length;
    const cols = grid[0].length;
    let maxCount = 0;

    const direction = [
        [1,0],
        [-1,0],
        [0,1],
        [0,-1]
    ];

    const bfs = (x,y) => {
        let size = 0;
        const queue = [];
        queue.push([x,y]);
        while(queue.length) {
            const [r,c] = queue.shift();

            if(r < 0 || c < 0 || r >= rows || c >= cols || grid[r][c] === 0) continue;

            grid[r][c] = 0;
            size += 1;
            for(let i = 0; i < 4;i++){
                const nr = r + direction[i][0];
                const nc = c + direction[i][1];
                queue.push([nr,nc])
            }
        }
        return size;
    }

    for(let i =0;i<rows;i++){
        for(let j=0;j<cols;j++){
            if(grid[i][j] === 1){
                const result = bfs(i,j);
                maxCount = Math.max(result, maxCount);
            }
        }
    }

    return maxCount;
};