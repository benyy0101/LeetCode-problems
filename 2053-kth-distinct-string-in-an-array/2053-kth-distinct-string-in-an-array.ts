function kthDistinct(arr: string[], k: number): string {
    
    const map = new Map();

    arr.forEach((e)=>{
        map.set(e, (map.get(e) || 0) + 1);
    })

    for(const e of arr){
        if(map.get(e) === 1 && --k === 0){
            return e;
        }
    }
    return "";
};