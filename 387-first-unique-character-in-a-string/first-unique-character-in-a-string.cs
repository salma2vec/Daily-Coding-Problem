public class Solution
{
    public int FirstUniqChar(string s)
    {
        Dictionary<int, int> res = new Dictionary<int, int>();
        for (int i = 0; i < s.Length; i++)
        {
            if (!res.ContainsKey(s[i]))
                res.Add(s[i], i);
            else
                res[s[i]] = -1;
        }
        foreach (var item in res)
        {
            if (item.Value != -1)
            {
                return item.Value;
            }
        }
        return -1;
        
    }
}