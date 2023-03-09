import itertools


with open('input.txt') as f:
    lines = f.readlines()
    
first_line = lines[0].split()

cur_stamina, max_stamina, max_turns, demons = map(int, first_line)

# Create an empty list to store the demon data
demon_data = []

#1st approach : sort demons based on the amount of mana they recover per round  and after that the sum of fragments that can be collected in n turns

# def sort_demons(demons):
#     demons.sort(key=lambda x: ( x[2]/x[3], sum(x[4:])))
#     return demons

# # Loop over the remaining lines in the input file and store the demon data in a list of tuples
# for i in range(1, demons+1):
#     demon_line = lines[i].split()
#     demon_stamina, turns_before_recover, stamina_recover = map(int, demon_line[:3])
#     #appended index at the beginning of the tuple to preserve it for output
#     demon_data.append((i-1,demon_stamina, turns_before_recover, stamina_recover))
#     fragments = map(int, demon_line[4:])
#     demon_data[i-1] = demon_data[i-1] + tuple(fragments)
    
# demon_data = sort_demons(demon_data)

# demons_faced = []

# for i in range(0, demons): demons_faced.append(-1)
    
# fragments = 0
# turns = 0
# stamina_recovery_turns = 0

# #you first recover your stamina, then face an enemy, then collect the fragments


# for i in range(0, demons):
#     demon = demon_data[i]
#     demon_stamina = demon[1]
#     demon_recover_turns = demon[2]
#     demon_recover_stamina = demon[3]
    
   
#     while turns < max_turns:
        
#         # First recover your stamina by Checking if enough turns have passed to recover stamina
#         if stamina_recovery_turns == demon_recover_turns:
#                 cur_stamina = min(cur_stamina + demon_recover_stamina, max_stamina)
#                 stamina_recovery_turns = 0

#         if(cur_stamina > demon_stamina):
#             if(demons_faced[i] == -1):
#                 # Fight demon and lose stamina 
#                 cur_stamina -= demon_stamina
#             # Collect fragments
#             fragments += demon[4 + demons_faced[i]]
#             # Increase the number of turns passed
#             turns += 1
#             # Increase the number of turns passed since last stamina recovery
#             stamina_recovery_turns += 1
#             # Increase the number of turns passed since you faced this demon
#             if(demons_faced[i] != -1):
#                 demons_faced[i] += 1
            


#2st approach (Better) : Sort the demons by the amount of fragments they give when defeated 
# Start iterating through the sorted list of demons
#If you have enough mana, defeat the demon and add the fragments to your total fragments.
#If you don't have enough mana, skip the demon and move on to the next one.


def sort_demons(demons):
    demons.sort(key=lambda x: (sum(x[4:])), reverse= True)
    return demons

def collectFragments(turns, demon):
    # print(sum(demon[4:turns+1]))
    return demon[4+turns+1]

# Loop over the remaining lines in the input file and store the demon data in a list of tuples
for i in range(1, demons+1):
    demon_line = lines[i].split()
    demon_stamina, turns_before_recover, stamina_recover = map(int, demon_line[:3])
    #append index at the beginning of the tuple to preserve it for output
    demon_data.append((i-1, demon_stamina, turns_before_recover, stamina_recover))
    fragments = map(int, demon_line[4:])
    demon_data[i-1] = demon_data[i-1] + tuple(fragments)
    
demon_data = sort_demons(demon_data)
    
demons_faced = []

for i in range(0, demons): demons_faced.append(-1)
    
collected_fragments = 0
turns_passed = 0
stamina_recovery_turns = 0
demon_order = []

for i in range(0, len(demon_data)):
    demon_index = demon_data[i][0]
    demon = demon_data[i]
    demon_stamina = demon[1]
    demon_recover_turns = demon[2]
    demon_recover_stamina = demon[3]
        
    print(demon_data[i], sum(demon_data[i][4:]))
        
    while demons_faced[i]+1 < max_turns:
        if stamina_recovery_turns == demon_recover_turns:
            cur_stamina = min(cur_stamina + demon_recover_stamina, max_stamina)
            stamina_recovery_turns = 0
        if(cur_stamina >= demon_stamina):
            if(demons_faced[i] == -1):
                # Fight demon and lose stamina 
                demons_faced[i] += 1
                cur_stamina -= demon_stamina
                demon_order.append(demon_index)
            else: 
                demons_faced[i] += 1
        else: 
            #if not enough stamina, move to the next demon
            break
        # Collect fragments
        collected_fragments += collectFragments(demons_faced[i], demon)
        # Increase the number of turns passed
        turns_passed += 1
        # Increase the number of turns passed since last stamina recovery
        stamina_recovery_turns += 1

print(collected_fragments, demon_order, demons_faced)

with open('output.txt', 'w') as f:
    for i in range(0, len(demon_order)):
        f.write(str(demon_order[i]) + "\n")

