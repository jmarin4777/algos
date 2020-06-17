describe("A function that validates IP addressess", () => {

    var ip1 = "172.16.254.1";
    var ip2 = "2001:0db8:85a3:0:0:8A2E:0370:7334";
    var ip3 = "256.256.256.256";
    var ip4 = "172.16.254.01";
    var ip5 = "02001:0db8:85a3:0000:0000:8a2e:0370:7334";
    var ip6 = "2001:0db8:85a3::8A2E:0370:7334";
    var ip7 = "2001:0db8:85a3:z:8A2E:0370:7334";
    var ip8 = "1.0.1.";
    var ip9 = "A.a.aA.2"

    const validateIPAddress = (IP) => {
        var checker = ["0","1","2","3","4","5","6","7","8","9","a","A","b","B","c","C","d","D","e","E","f","F"]
        var temp;
        var IPArr = IP.split('.');
        if(IPArr.length === 4){
            for(let i of IPArr){
                if(Number(i) < 0 || Number(i) > 255 || i.length === 0 || isNaN(i)){
                    return "Neither"
                }
                if(Number(i) < 10 && i.length > 1){
                    return "Neither"
                }
                if(Number(i) > 9 && Number(i) < 100 && i.length > 2){
                    return "Neither"
                }
                if(Number(i) > 99 && i.length > 3){
                    return "Neither"
                }
            }
            return "IPv4"
        } else{
            IPArr = IP.split(':');
            if(IPArr.length === 8){
                for(let i of IPArr){
                    if(i.length === 0 || i.length > 4){
                        return "Neither"
                    }
                    temp = i.split('')
                    for(let i of temp){
                        if(!checker.includes(i)){
                            return "Neither"
                        }
                    }
                }
                return "IPv6"
            } else{
                return "Neither"
            }
        }
        
    };

    it("should be IPv4", () => {
        expect(validateIPAddress(ip1)).toEqual("IPv4");
    });

    it("should be IPv6", () => {
        expect(validateIPAddress(ip2)).toEqual("IPv6");
    });

    it("should be Neither", () => {
        expect(validateIPAddress(ip3)).toEqual("Neither");
        expect(validateIPAddress(ip4)).toEqual("Neither");
        expect(validateIPAddress(ip5)).toEqual("Neither");
        expect(validateIPAddress(ip6)).toEqual("Neither");
        expect(validateIPAddress(ip7)).toEqual("Neither");
        expect(validateIPAddress(ip8)).toEqual("Neither");
        expect(validateIPAddress(ip9)).toEqual("Neither");
    });
})