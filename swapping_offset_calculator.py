print("Prerequisites:")
print("page size should be multiple of 2")
print("address space should be m bit or 2^m bytes")
print()

import math

# return the page number and offset value return the page number and offset value
def calculate(page_size, address_reference):
    # For page size 4KB -> (2^2 * 2^10 = 4096)
    # We need the value of (size in 2^size * 2^10)
    size = int(math.sqrt(page_size))

    # Calculate the page number
    # page number = quotient of address reference / page size
    page_number = address_reference >> (size + 10)  # 2^size * 2^10 = 2^(size+10)

    # Calculate the offset
    # offset = remainder of address reference / page size
    offset = address_reference & int(hex((page_size * 1024) - 1), 16)

    return page_number, offset


# page_size = 4  # 4KB
# address_reference = 0x12345678  # 305419896

if __name__ == '__main__':
    page_size = int(
        input("Enter the page size in (KB)\nExample: 4 (4096 bytes): "))
    address_reference = int(input(
        "Enter the address reference in (hex)\nExample: 0x12345678 (305419896): "), 16)
    page_number, offset = calculate(page_size, address_reference)
    
    print("Address", hex(address_reference), "contains:")
    print("Page Number: ", page_number)
    print("Offset: ", hex(offset))