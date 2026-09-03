'''Assignment 4: Dynamic Data Pipeline with Lambdas & Custom Sorting
Scenario
An AI classification pipeline processes raw data inputs. Each raw input is a tuple of 
string annotations describing a product name, its price, and rating. The pipeline needs to 
clean, filter, and sort these records.'''

def process_dataset(dataset)->list:
    out=[]
    for i in dataset:
        product=i[0]
        price=float(i[1].split(" ")[1])
        score=float(i[2].split(" ")[1])
        list1=[product,price,score]
        out.append(list1)
    filt=list(filter(lambda x:x[1]<=1000.0,out))
    mp=list(map(lambda x:{"product":x[0], "price":x[1], "score":x[2]},filt))
    sorted_map=list(sorted(mp,key =lambda inp:inp['score'],reverse=True))
    print(sorted_map)

def main():
    data_input = [
    ("Laptop", "Price: 1200", "Rating: 4.8"),
    ("Phone", "Price: 800", "Rating: 4.5"),
    ("Mouse", "Price: 25", "Rating: 4.7"),
    ("Charger", "Price: 15", "Rating: 4.2")
]
    process_dataset(data_input)
main()