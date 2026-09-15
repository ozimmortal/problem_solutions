func groupAnagrams(strs []string) [][]string {
    sortStr := func(str string) string{
        chars := []byte(str)
        sort.Slice(chars, func(i , j int)bool{
            return chars[i] < chars[j]
        })
        return string(chars)
    }
    group := map[string][]string{}
    for i:=0; i < len(strs); i++{
        key := sortStr(strs[i]) 
        group[key] = append(group[key], strs[i])
    }

    res := [][]string{}
    for _, value := range group{
        res = append(res , value)
    }
    return res
}