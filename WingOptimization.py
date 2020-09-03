#Try using Target_Cl() to find AOA for a given CL

#MachUp is a AeroModel libary 
import machupX

#To handle input files 
import json

#To export data 
import pandas 

#For acessing sign functions
import math

#Calculate wing forces over a airspeed range
def WingForces(scene, airspeed, weight, tolerance):
    
    #To store the results 
    data = []

    # Solve for forces at varying velocities
    for i in airspeed:

        #Set the intial conditions
        velocity = i
        alpha = 0
        stepsize = 20
        lift = 0

        #Iterate alphas until Lift Force = Weight or Alpha is too large
        while abs(lift - weight) > tolerance and alpha < 45:
            
            #Set the alpha
            alpha += stepsize
            
            #Change the Velocity and Alpha 
            state = {
                "type" : "aerodynamic",
                "velocity" : velocity,
                "alpha" : alpha
            }

            #Check the Forces acting at this state 
            scene.set_aircraft_state(state = state)
            forces = scene.solve_forces(dimensional=True, non_dimensional=False, verbose=True)
            lift = forces["Wing"]["total"]["FL"]

            #Check stepsize should be positive or negitive 
            stepsize_old = stepsize
            stepsize = math.copysign(stepsize, weight - lift) 

            #If we just passed from one side of the target to the other then reduce step size
            if math.copysign(1, stepsize_old) != math.copysign(1, stepsize):
                stepsize *= 0.5

        #Record the Data
        dict1 = {'Velocity': velocity, 'Alpha': alpha}
        dict2 = forces["Wing"]["total"]
        dict1.update(dict2)
        data.append(dict1)

    #Return recorded results
    return data

#Return chord distrabution for Bell lift distrabution (Zero Twist)  
def BellDistrabution(root_chord, chordpoints):

    #For storing data
    chord_distrabution = []

    #For how many chord points are needed 
    for i in range(0, chordpoints + 1):

        #Calculate chord position
        chord_position = (i / chordpoints)
        
        #Calculate chord length
        chord_length = ((1 - (chord_position) ** 2) ** 1.5) * root_chord

        #Record Results    
        chord_distrabution.append([chord_position, chord_length])

    #Return the result
    return chord_distrabution

#Returns Sweep Distrabution for Cresent Moon
def CresentSweep(max_sweep, chordpoints):
 
    #For storing data
    sweep_distrabution = []

    #For how many chord points are needed 
    for i in range(0, chordpoints + 1):

        #Calculate chord position
        chord_position = (i / chordpoints)
        
        #Calculate chord length
        sweep = (1 - (1 - (chord_position) ** 2) ** 0.5) * max_sweep

        #Record Results    
        sweep_distrabution.append([chord_position, sweep])

    #Return the result
    return sweep_distrabution   

#Wing dihedral angles 
def CresentDihedral(max_dihedral, chordpoints):

    #For storing data
    dihedral_distrabution = []

    #For how many chord points are needed 
    for i in range(0, chordpoints + 1):

        #Calculate chord position
        chord_position = (i / chordpoints)
        
        #Calculate chord length
        dihedral = (1 - (1 - (chord_position) ** 2) ** 0.5) * max_dihedral

        #Record Results    
        dihedral_distrabution.append([chord_position, dihedral])

    #Return the result
    return dihedral_distrabution      


#Main Function
if __name__=="__main__":

    #Open the wing file and store JSON file
    with open('Wings/Wing.json') as file:
        json_file = json.load(file)
        file.close()

    # Initialize Scene object. This contains the airplane and all necessary
    scene = machupX.Scene("Wings/Wing_Setup.json")

    #Show Wireframe
    scene.display_wireframe(show_vortices = False ,show_legend = True)

    # Create a Pandas Excel writer using XlsxWriter as the engine.
    Writer = pandas.ExcelWriter('Results/Results.xlsx', engine='xlsxwriter')

    #Wing Profile Variance   
    # for semispan in range(3, 4, 1):
    #     for sweep in range(0, 90, 10):

    #Change the wingspan
    json_file["wings"]["main_wing"]["semispan"] = 3

    #Change the Wing Chord 
    json_file["wings"]["main_wing"]["chord"] = BellDistrabution(2 / 3, 50)
    #json_file["wings"]["main_wing"]["chord"] = ['elliptic', 2 / semispan]
    json_file["wings"]["main_wing"]["sweep"] = CresentSweep(30, 50)
    json_file["wings"]["main_wing"]["dihedral"] = CresentDihedral(30, 50)

    #Update the JSON file 
    json.dump(json_file, open('Wings/Wing.json', 'w'), indent = 4)

    #Update the Wing File 
    scene = machupX.Scene("Wings/Wing_Setup.json")

    #Solve for forces (Airspeed Range (m/s), Weight (N), Tollerance)
    Forces = WingForces(scene, range(20, 100), 1000, 0.5)

    #Change the Data to a DataFrame
    DataFrame = pandas.DataFrame(Forces)

    #Write the Dataframe to a unique sheet
    DataFrame.to_excel(Writer, sheet_name='Sweep = ' + str(30))

    # Close the Pandas Excel writer and output the Excel file.
    Writer.save()       

    