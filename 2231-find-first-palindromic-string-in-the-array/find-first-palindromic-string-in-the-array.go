func firstPalindrome(words []string) string {
    for i:=0;i<len(words);i++{
        str:=words[i]
        ru:=[]rune(str)
        s:=0
        e:=len(ru)-1
        for s<e{
            ru[s],ru[e]=ru[e],ru[s]
            s++
            e--
        }
        restr:=string(ru)
        if str==restr{
            return str
        }
    }
    return ""
}