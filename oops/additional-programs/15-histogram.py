
def draw_histogram(nums):
    scale_factor = 2

    max_num = max(nums)
    max_with_scale = max_num * scale_factor
    loop_max = max_with_scale+1

    print("\nScale factor:", scale_factor, "\n")
    
    for i in range(1, loop_max):
        line = "%8.0f|\t" % (loop_max-i)
        for num in nums:
            if (loop_max-i == num*scale_factor):
                line = line + f"-{num}-\t"
            elif (loop_max-i <= num*scale_factor):
                line = line + "| |\t"
            else:
                line = line + "   \t"
        print(line)
    
    dashes = "-" * len(nums) * 8
    dashes = dashes + ("-" * len(nums))
    print("\t "+dashes)
    
    line = "\t\t"
    for num in nums:
        line = line + " " + str(num) + "\t"
    print(line)


nums = input("Enter comma seperated numbers: ")
nums = nums.split(",")
nums = map(lambda x: int(x), nums)
nums = list(nums)
draw_histogram(nums)
