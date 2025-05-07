try:
    x = int("python")        # ValueError
    y = 25 / 0            # ZeroDivisionError
    print(undefined_var)  # NameError
    a = [1, 2, 3]
    print(a[5])           # IndexError
except IndexError:
    print("Index error occurred")
except ValueError:
    print("ValueError occurred.")
except ZeroDivisionError:
    print("ZeroDivisionError occurred.")
except NameError:
    print("NameError occurred.")
except Exception as e:
    print("Some other error:", e)
else:
    print("All operations successful. Result is:", result)

finally:
    print("This will always execute")



