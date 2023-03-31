def insertion_sort(nums):
    for i in range(1, len(nums)):
        index = i
        if nums[index] < nums[index-1]: 
            nums.insert(index-1, nums[index])
            del nums[i+1]
            break
    
    return nums



if "__main__" == __name__:
    nums = [1,2,4,3,5,6]
    sorted_list = insertion_sort(nums)
    print(sorted_list)
    assert sorted_list == [1,2,3,4,5,6]
                

                
