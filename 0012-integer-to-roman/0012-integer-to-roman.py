class Solution(object):
    def intToRoman(self, num):
        val_to_sym = {
            1000: "M", 900: "CM", 500: "D", 400: "CD",
            100: "C", 90: "XC", 50: "L", 40: "XL",
            10: "X", 9: "IX", 5: "V", 4: "IV", 1: "I"
        }

        res = ""
        for val in sorted(val_to_sym.keys(), reverse=True):
            while num >= val:
                num -= val
                res += val_to_sym[val]
        return res
