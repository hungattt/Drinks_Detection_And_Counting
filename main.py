# data = {258: 'coca cola can', 499: '7up can', 99: 'pepsi can'}
#
# sorted_values = sorted(data.values(), key=lambda x: list(data.keys())[x])
#
# print(sorted_values)


my_dict = {258: 'coca cola can', 499: '7up can', 99: 'pepsi can'}
print(sorted(my_dict.items()))
# Sắp xếp các giá trị theo thứ tự tăng dần của khóa
sorted_values = [value for key, value in sorted(my_dict.items())]

print(sorted_values)