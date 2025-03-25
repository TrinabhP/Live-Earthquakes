from quakeFuncs import *

def main():

   earthquakes = read_quakes_from_file("quakes.txt")


   display_quakes(earthquakes)
   print("\nOptions:\n  (s)ort\n  (f)ilter\n  (n)ew quakes \n  (q)uit\n")

   choice = input("Choice: ")

   while (choice != 'q' and choice != 'Q'):
      if (choice == 's' or choice == 'S'):
         sort = input("Sort by (m)agnitude, (t)ime, (l)ongitude, or l(a)titude? ")
         if (sort == 'm' or sort == 'M'):
            earthquakes = sort_by_mag(earthquakes)
            display_quakes(earthquakes)
         elif (sort == 't' or sort == 'T'):
            earthquakes = sort_by_time(earthquakes)
            display_quakes(earthquakes)
         elif (sort == 'l' or sort == 'L'):
            earthquakes = sort_by_longitude(earthquakes)
            display_quakes(earthquakes)
         elif (sort == 'a' or sort == 'A'):
            earthquakes = sort_by_latitude(earthquakes)
            display_quakes(earthquakes)

      elif (choice == 'f' or choice == 'F'):
         filt = input("Filter by (m)agnitude or (p)lace? ")
         earthquakes1 = [quake for quake in earthquakes]
         if (filt == 'm' or filt == 'M'):
            lower = float(input("Lower bound: "))
            upper = float(input("Upper bound: "))
            earthquakes1 = filter_by_mag(earthquakes, lower, upper)
            display_quakes(earthquakes1)

         elif (filt == 'p' or filt == 'P'):
            search = input("Search for what string? ")
            earthquakes1 = filter_by_place(earthquakes, search)
            display_quakes(earthquakes1)


      elif (choice == 'n' or choice == 'N'):

         features = get_json('http://earthquake.usgs.gov/earthquakes/feed/v1.0/summary/1.0_hour.geojson')["features"]
         for feature in features:
            new_quake = quake_from_feature(feature)
            count = 0
            if (new_quake not in earthquakes):
               earthquakes.append(quake_from_feature(feature))
               count += 1

         if (count > 0):
            print("\nNew quakes found!!!")

         display_quakes(earthquakes)



      print("\nOptions:\n  (s)ort\n  (f)ilter\n  (n)ew quakes \n  (q)uit\n")
      choice = input("\nChoice: ")

      save_data(earthquakes, "quakes.txt")

   
if __name__ == "__main__":
   main()