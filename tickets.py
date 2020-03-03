def tickets(people):
  if len(people) == 0:
      return "NO"
  vasya = {'25':0 , '50':0 , '100':0}
  while len(people) > 0:
      if people[0] == 25:
          vasya['25'] += 1
          people.pop(0)
          continue
      elif people[0] == 50:
          vasya['50'] += 1
          people.pop(0)
          if vasya['25'] == 0:
              return 'NO'
              break 
          else:
            vasya['25'] -= 1
            continue
      elif people[0] == 100:
          vasya['100'] += 1
          people.pop(0)
          if (vasya['50'] > 0 and vasya['25'] > 0) or (vasya['25'] > 2):
              if vasya['50'] > 0:
                  vasya['50'] -= 1
                  vasya['25'] -= 1
                  continue
              else:
                  vasya['25'] -= 3
                  continue
          else:
              return "NO"
              break       
  else:
      return 'YES'


print(tickets([25,25,50,100,25,25,50,100,25,25,25,100,100,25]))
