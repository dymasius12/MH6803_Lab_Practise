# This program displays the total of the
# amounts in the sales_data.txt file.

def main():
    # Initialize an accumulator.
    total = 0.0
    
    try:
        # Open the sales_data.txt file.
        infile = open('11_sales_data.txt', 'r')

        # Read the values from the file and
        # accumulate them.
        for line in infile:
            amount = float(line)
            print(amount)
            total += amount

        # Close the file.
        infile.close()
    except Exception as err:
        print(err)
    else:
        # Print the total.
        print("total = ", format(total, ',.2f'))

    try:
        # Open the sales_data.txt file.
        infile = open('11_sales_data.txt', 'a')

        # write the string s to the file
        infile.write("Audit record") 
        list =["1234\n","45677\n","334.55\n"]
        infile.writelines(list) 
    except Exception as err:
        print(err)
    else:
        # Close the file.
        infile.close()


# Call the main function.
main()
