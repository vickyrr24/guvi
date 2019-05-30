first_nums = ["Zero", "One", "Two", "Three", "Four", "Five", "Six", "Seven", "Eight", "Nine", "Ten", "Eleven", "Twelve",
              "Thirteen", "Fourteen", "Fifteen", "Sixteen", "Seventeen", "Eighteen", "Nineteen"]
tens = ["Ten", "Twenty", "Thirty","Forty","Fifty", "Sixty","Seventy","Eighty","Ninety"]

num=int(input())
print(num)
if num < 20:
    print(first_nums[num])
elif num < 100 and num % 10 == 0:
    print(tens[int(num/10 - 1)])
elif num < 1000 and num % 100 == 0:
    print(first_nums[int(num/100)] + " hundred")
elif num == 1000:
    print("One Thousand")
elif num < 100 and num % 10 != 0:
    print(tens[int(num//10 - 1)] + " " + first_nums[int(num%10)])
elif num < 1000:
    if num%100 < 20:
        print(first_nums[int(num//100)] + " Hundred and " + first_nums[num%100])
    else:
        print(first_nums[int(num//100)] + " Hundred and " + tens[int(num%100//10 - 1)] + " " + first_nums[int(num%10)])
