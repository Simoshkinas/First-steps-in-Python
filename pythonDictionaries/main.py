monthConversions = {
                        "Jan": "January",
                        "Feb": "February",
                        "Mar": "March",
                        "Apr": "April",
                        "May": "May",
                        "Jun": "June",
                        "Jul": "July",
                        "Aug": "August",
                        "Sep": "September",
                        "Oct": "October",
                        "Nov": "November",
                        "Dec": "December"
                    }


monthConversions2 = {
                        1: "January",
                        2: "February",
                        3: "March",
                        4: "April",
                        5: "May",
                        6: "June",
                        7: "July",
                        8: "August",
                        9: "September",
                        10: "October",
                        11: "November",
                        12: "December"
                    }
print(monthConversions["Sep"])
print(monthConversions.get("Aug"))
print(monthConversions.get("Luv"))
print(monthConversions.get("Luv", "Not a valid key"))

print(monthConversions2[8])
print(monthConversions2.get(7))
print(monthConversions2.get(15))
print(monthConversions2.get(15, "Not a valid key"))
