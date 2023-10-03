# LOCATE SHORT PATH:
# Set current distance and point to 0 and start
    # WHILE LOOP: start
    # IF 'current distance' > 'current point' THEN continue
        # FOR LOOP:
        # IF 'pointA' = 'current point' THEN add 'current distance' to 'weight'
            # IF distance < pointB THEN set previousPoint to current point
    # Create shortest path

    # WHILE LOOP: end
    # Set 'end' to 'previousPoint(end)'
    # RETURN: 'distances' and 'shortest path'

# List all paths
# Set 'locations' to Home, Store A, Store B, School, Intersection
    # WHILE LOOP: True
    # Print "LOCATIONS: Home, Store A, Store B, School, Intersection"
    # Ask input for starting point with "Where is your starting point?:"
        # IF 'start point' is in 'locations'
            # WHILE LOOP: true
            # Set end point to be input by user, ask "Where do you want to go:"
                # IF 'end point' is in 'locations' THEN break
                # ELSE print "Invalid enpoint. Please type another location." 
            # BREAK
        # ELSE print "Invalid starting point. Please type another location."
    # Call `short path` and get values of 'paths', 'start point', and 'end point'
# IF  length of 'shortest path' = 1
    # IF 'start point' = 'end point' THEN...
    # print, with the values, "Shortest Distance" and "Shortest path"
    # ELSE print "Invalid path. Please try again"
# ELSE print, with the values, "Shortest Distance" and "Shortest Path"
