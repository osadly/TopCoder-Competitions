class BuffaloBuffalo {
    public:
    string check(string s) {
        int n=s.length();
        if(n%8!=7) { return "Not good"; }
        
        string b="buffalo ";
        
        for(int i=0; i<n; i++) {
            if(b[i%8]!=s[i]) { return "Not good"; }
        }
        return "Good";
    }
};
