adjective0 = input("Give me an adjective: ")
adjective1 = input("Give me an adjective: ")
adjective2 = input("Give me an adjective: ")
adjective3 = input("Give me an adjective: ")
noun0 = input("Give me a noun: ")
noun1 = input("Give me a noun: ")
pluralnoun0 = input("give me a plural noun")
personinroomfemale = input("give me the name of a female person in the room")
articalofclothing = input("give me a artical of clothing")
city = input("give me a city")
pluralnoun = input("give me a plural noun")



story = f"There are many {adjective0} ways to choose a/n {noun0} to read. first you could ask for recomendations from  \
your family and {pluralnoun0}. Just don't ask aunt {personinroomfemale}. She only reads {adjective1} books with {articalofclothing}-  \
ripping goddeses on the cover. if your freinds and faimily are no help, try checking out the {noun1} Review in the {city} times.    \
if the {pluralnoun} featured there are too {adjective2} for your taste, try something a little more {adjective3}"

print(story)