# we can short circuit a function with return. return stops executing.
def chai_status(cups: int = 0):
    if cups == 0:
        return "sorry chai over"  # Early exit

    return "chai is ready"
    print("chai on")  # never reaches


print(chai_status())
print(chai_status(5))


##-------------------------- Returning multiple values
# returns tuple
def chai_report():
    return 100, 20  # sold, remaining


sold, remains = chai_report()
print(sold)
print(remains)


##------------------------ unhandled
# returns tuple
def chai_report_3():
    return 100, 20, 10  # sold, remaining


sold, remains = chai_report_3()  # ValueError: too many values to unpack

# To handle this, use _
sold, remains, _ = chai_report_3()
