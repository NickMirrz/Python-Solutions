service_schedule = {"-": 0, "Oil change" : 35, "Tire rotation" : 19, "Car wash" : 7, "Car wax": 12}
first_service = ""
second_service = ""
invoice_total = 0

#Output a menu of automotive services and the corresponding cost of each service.
print("Davy's auto shop services")
print("Oil change -- $35")
print("Tire rotation -- $19")
print("Car wash -- $7")
print("Car wax -- $12")
print("")

#Prompt the user for two services from the menu. 
first_service = input("Select first service: \n")
print("")
second_service = input("Select second service: \n\n")
print("")

#Output an invoice for the services selected.   
print("Davy's auto shop invoice\n")
#print("\n")

#allow the user to enter a dash (-), which indicates no service Service 1.
if(first_service == "-"):
  print("Service 1: No service")
  
#Output the cost for each service  
else:
  print("Service 1: %s, $%d" % (first_service, service_schedule.get(first_service)))

#allow the user to enter a dash (-), which indicates no service for Service 2.  
if(second_service == "-"):
  print("Service 2: No service\n")
  
#Output the cost for each service      
else:
  print("Service 2: %s, $%d\n" % (second_service, service_schedule.get(second_service)) )

#Calculate total cost
invoice_total = service_schedule.get(first_service) + service_schedule.get(second_service)

#Output of the total cost.
print("Total: $%d" % (invoice_total))
