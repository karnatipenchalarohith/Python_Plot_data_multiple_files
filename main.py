import os
import os.path
from pathlib import Path
import re
import numpy as np
import matplotlib.pyplot as plt

import pylab as pl


import xlwt


#walter_meas

Device_name="ESDPMOS"

walter_meas_path= r"C:\\All_projects\tc18d_model_assessment\Data\correct\ESDPMOS\\"

werner_meas_path= r"C:\\All_projects\tc18d_model_assessment\Data\correct\ESD_all_correct\ESDPMOS\\"

model_simulation_path=r"C:\\All_projects\tc18d_model_assessment\assessment\ESDPMOS\LOG_add_contact_resistance_metal_small\save_init_compa_tC18d_ESDPMOS\data\\"

fullmap_point_data_path =r"C:\\All_projects\tc18d_model_assessment\Data\correct\ESD_all_correct\Point_data\M009\ESDPMOS\\"

TYPE=-1

# directory_in_str="C:/All_projects/tc18d_model_assessment/Data/correct/ESD_all_correct/Point_data/M009/ESDNMOS"

# directory = os.fsencode(directory_in_str)

#for file in os.listdir(directory):
 #   filename = os.fsdecode(file)
 #   if filename.endswith(".txt") or filename.endswith(".py"):
        # print(os.path.join(directory, filename))


#directory_full_walter="C:\All_projects\tc18d_model_assessment\Data\correct\ESDNMOS"
Idlin_initial_meas_die1_walter = []
Idsat_initial_meas_die1_walter = []

Idlin_initial_meas_die20_werner = []
Idsat_initial_meas_die20_werner = []

Idlin_TT=[]
Idsat_TT=[]

Idlin_SS=[]
Idsat_SS=[]

Idlin_FF=[]
Idsat_FF=[]

for iter in range(1,13):
    Vgs = []

#Walter Measurement
    for site in range(1,2):
        flname = "M002xW6C442_W13x0{:02d}x".format(site) + Device_name + "x{:02d}xTP25.txt".format(iter)
        print(flname)
        with open( walter_meas_path + flname) as f:
            lines_after_17=[]
            clean_lines=[]
            lines_after_17 = f.readlines()[92:93]
            print(lines_after_17)
            clean_lines = [x.strip(' ') for x in lines_after_17]
            for row in clean_lines:
                row = re.split(' +', row)
                # row = row.split('/s* ')
                #     print(row)
                Idlin_initial_meas_die1_walter.append(row[15])
                Idlin_initial_meas_die1_walter2 = np.array(Idlin_initial_meas_die1_walter)
                print(Idlin_initial_meas_die1_walter2)

        with open( walter_meas_path + flname) as f:
            lines_after_17=[]
            clean_lines=[]
            lines_after_17 = f.readlines()[1195:1196]
            print(lines_after_17)
            clean_lines = [x.strip(' ') for x in lines_after_17]
            for row in clean_lines:
                row = re.split(' +', row)
                # row = row.split('/s* ')
                #     print(row)
                Idsat_initial_meas_die1_walter.append(row[15])
                Idsat_initial_meas_die1_walter2 = np.array(Idsat_initial_meas_die1_walter)
                print(Idsat_initial_meas_die1_walter2)
#################

# Werner's Measurement

    for site in range(20,21):
        flname = "M006xW6C442W13x0{:02d}x".format(site) + Device_name + "x{:02d}xTP25.txt".format(iter)
        print(flname)
        with open( werner_meas_path + flname) as f:
            lines_after_17=[]
            clean_lines=[]
            lines_after_17 = f.readlines()[92:93]
            print(lines_after_17)
            clean_lines = [x.strip(' ') for x in lines_after_17]
            for row in clean_lines:
                row = re.split(' +', row)
                # row = row.split('/s* ')
                #     print(row)
                Idlin_initial_meas_die20_werner.append(row[15])
                Idlin_initial_meas_die20_werner2 = np.array(Idlin_initial_meas_die20_werner)
                print(Idlin_initial_meas_die20_werner2)

        with open( werner_meas_path + flname) as f:
            lines_after_17=[]
            clean_lines=[]
            lines_after_17 = f.readlines()[1195:1196]
            print(lines_after_17)
            clean_lines = [x.strip(' ') for x in lines_after_17]
            for row in clean_lines:
                row = re.split(' +', row)
                # row = row.split('/s* ')
                #     print(row)
                Idsat_initial_meas_die20_werner.append(row[15])
                Idsat_initial_meas_die20_werner2 = np.array(Idsat_initial_meas_die20_werner)
                print(Idsat_initial_meas_die20_werner2)

 #   tC18d_ESDNMOS_PLOT__G1_L01_TR__IDVG_LIN_T_p025_tt_lib_25C
    # Model Simulation values
    for site in range(20,21):
  #      flname = "tC18d_ESDNMOS_PLOT__G{:d}_L{:02d}_OUT_IDVD_VB0_T_p025_tt_lib_25C.txt".format(iter, iter)

        flname = "tC18d_" + Device_name + "_PLOT__G{:d}".format(iter) + "_L{:02d}_TR__IDVG_LIN_T_p025_tt_lib_25C.txt".format(iter)
        print(flname)
        with open( model_simulation_path + flname) as f:
            lines_after_17=[]
            clean_lines=[]
            lines_after_17 = f.readlines()[46:47]
            print(lines_after_17)
            clean_lines = [x.strip(' ') for x in lines_after_17]
            for row in clean_lines:
                row = re.split(' +', row)
                # row = row.split('/s* ')
                #     print(row)
                Idlin_TT.append(row[1])
                Idlin_TT2 = np.array(Idlin_TT)

                Idlin_TT5 = list(map(float, Idlin_TT2))

                if TYPE==-1:
                    Idlin_TT3 = [i * -1 for i in Idlin_TT5]
                else:
                    Idlin_TT3 = Idlin_TT5




                print(Idlin_TT2)
                print(Idlin_TT3)
               # Idlin_TT5=Idlin_TT2


                print(Idlin_TT2)
# tC18d_ESDNMOS_PLOT__G1_L01_OUT_IDVD_VB0_T_p025_tt_lib_25C
            flname = "tC18d_" +  Device_name + "_PLOT__G{:d}_".format(iter) +  "L{:02d}_OUT_IDVD_VB0_T_p025_tt_lib_25C.txt".format(iter)
            print(flname)

        with open( model_simulation_path + flname) as f:
            lines_after_17=[]
            clean_lines=[]
            lines_after_17 = f.readlines()[36:37]
            print(lines_after_17)
            clean_lines = [x.strip(' ') for x in lines_after_17]
            for row in clean_lines:
                row = re.split(' +', row)
                # row = row.split('/s* ')
                #     print(row)
                Idsat_TT.append(row[3])
                Idsat_TT2 = np.array(Idsat_TT)



                Idsat_TT5 = list(map(float, Idsat_TT2))

                if TYPE == -1:
                    Idsat_TT3 = [i * -1 for i in Idsat_TT5]
                else:
                    Idsat_TT3=Idsat_TT5






                print(Idsat_TT2)

        # SS Model Sim Values

        flname = "tC18d_" + Device_name + "_PLOT__G{:d}_".format(iter) + "L{:02d}_TR__IDVG_LIN_T_p025_ss_lib_25C.txt".format(iter)
        print(flname)
        with open(model_simulation_path + flname) as f:
            lines_after_17 = []
            clean_lines = []
            lines_after_17 = f.readlines()[46:47]
            print(lines_after_17)
            clean_lines = [x.strip(' ') for x in lines_after_17]
            for row in clean_lines:
                row = re.split(' +', row)
                # row = row.split('/s* ')
                #     print(row)
                Idlin_SS.append(row[1])
                Idlin_SS2 = np.array(Idlin_SS)

                Idlin_SS5 = list(map(float, Idlin_SS2))

                Idlin_SS3 = [i * -1 for i in Idlin_SS5]

                print(Idlin_SS5)
            # tC18d_ESDNMOS_PLOT__G1_L01_OUT_IDVD_VB0_T_p025_tt_lib_25C
            flname = "tC18d_" + Device_name + "_PLOT__G{:d}_".format(iter) + "L{:02d}_OUT_IDVD_VB0_T_p025_ss_lib_25C.txt".format(iter)
            print(flname)

        with open(model_simulation_path + flname) as f:
            lines_after_17 = []
            clean_lines = []
            lines_after_17 = f.readlines()[36:37]
            print(lines_after_17)
            clean_lines = [x.strip(' ') for x in lines_after_17]
            for row in clean_lines:
                row = re.split(' +', row)
                # row = row.split('/s* ')
                #     print(row)
                Idsat_SS.append(row[3])
                Idsat_SS2 = np.array(Idsat_SS)

                Idsat_SS5 = list(map(float, Idsat_SS2))

                if TYPE == -1:
                    Idsat_SS3 = [i * -1 for i in Idsat_SS5]
                else:
                    Idsat_SS3 =Idsat_SS5


                print(Idsat_SS5)

        #FF sim Values

        flname = "tC18d_" + Device_name + "_PLOT__G{:d}_".format(iter) + "L{:02d}_TR__IDVG_LIN_T_p025_ff_lib_25C.txt".format(iter)
        print(flname)
        with open(model_simulation_path + flname) as f:
            lines_after_17 = []
            clean_lines = []
            lines_after_17 = f.readlines()[46:47]
            print(lines_after_17)
            clean_lines = [x.strip(' ') for x in lines_after_17]
            for row in clean_lines:
                row = re.split(' +', row)
                # row = row.split('/s* ')
                #     print(row)
                Idlin_FF.append(row[1])
                Idlin_FF2 = np.array(Idlin_FF)

                Idlin_FF5 = list(map(float, Idlin_FF2))

                if TYPE == -1:
                    Idlin_FF3 = [i * -1 for i in Idlin_FF5]
                else:
                    Idlin_FF3 = Idlin_FF5




                print(Idlin_FF3)

                print(Idlin_FF2)
            # tC18d_ESDNMOS_PLOT__G1_L01_OUT_IDVD_VB0_T_p025_tt_lib_25C
            flname = "tC18d_" + Device_name + "_PLOT__G{:d}_".format(iter) + "L{:02d}_OUT_IDVD_VB0_T_p025_ff_lib_25C.txt".format(iter)
            print(flname)

        with open(model_simulation_path + flname) as f:
            lines_after_17 = []
            clean_lines = []
            lines_after_17 = f.readlines()[36:37]
            print(lines_after_17)
            clean_lines = [x.strip(' ') for x in lines_after_17]
            for row in clean_lines:
                row = re.split(' +', row)
                # row = row.split('/s* ')
                #     print(row)
                Idsat_FF.append(row[3])
                Idsat_FF2 = np.array(Idsat_FF)

                Idsat_FF5 = list(map(float, Idsat_FF2))

                if TYPE == -1:
                    Idsat_FF3 = [i * -1 for i in Idsat_FF5]
                else:
                    Idsat_FF3 = Idsat_FF5




                print(Idsat_FF3)
                print(Idsat_FF5)

print(Idlin_initial_meas_die1_walter2[0])
print(Idlin_initial_meas_die1_walter2[3])
print(Idlin_initial_meas_die1_walter2[5])

print(Idsat_initial_meas_die1_walter2[0])
print(Idsat_initial_meas_die1_walter2[3])
print(Idsat_initial_meas_die1_walter2[5])


print(Idlin_initial_meas_die20_werner2[0])
print(Idlin_initial_meas_die20_werner2[3])
print(Idlin_initial_meas_die20_werner2[5])

print(Idsat_initial_meas_die20_werner2[0])
print(Idsat_initial_meas_die20_werner2[3])
print(Idsat_initial_meas_die20_werner2[5])

print(Idlin_TT2)
print(Idsat_TT2)

print(Idlin_SS2)
print(Idsat_SS2)


print(Idlin_FF2)
print(Idsat_FF2)


Idlin_initial_meas_die1_walter3 = list(map(float, Idlin_initial_meas_die1_walter2))
Idsat_initial_meas_die1_walter3 = list(map(float, Idsat_initial_meas_die1_walter2))


Idlin_initial_meas_die20_werner3 = list(map(float, Idlin_initial_meas_die20_werner2))
Idsat_initial_meas_die20_werner3 = list(map(float, Idsat_initial_meas_die20_werner2))


print(Idlin_TT2)
print(Idlin_TT5)


"""

"""
#Idlin_TT3 = list(map(float, Idlin_TT5))
#Idsat_TT3 = list(map(float, Idsat_TT2))


#Idlin_SS3 = list(map(float, Idlin_SS2))
#Idsat_SS3 = list(map(float, Idsat_SS2))


#Idlin_FF3 = list(map(float, Idlin_FF2))
#Idsat_FF3 = list(map(float, Idsat_FF2))



Idlin_initial_meas_die1_walter=0.00185403
Idsat_initial_meas_die1_walter=0.0093832

Idlin_initial_meas_die20=1.7776e-3
Idsat_initial_meas_die20=0.010085

Idlin_initial_red_die20=0.0017191
Idsat_initial_red_die20=0.010057

Idlin_initial_red_die21=0.0016723
Idsat_initial_red_die21=0.010053

Idlin_initial_red_die22=0.0017381
Idsat_initial_red_die22=0.010136


Idlin_model_TT=[2.1572759e-03]
Idlin_model_SS=[1.8527796e-03]
Idlin_model_FF=[2.4646430e-03]

Idsat_model_TT=[1.1446495e-02]
Idsat_model_SS=[9.5960417e-03]
Idsat_model_FF=[1.2995159e-02]



# Point data Meas

for iter in range(1,13):
    Vgs = []
    Ids = []

    for site in range(1,40):
        flname = "M009xW6C442W13x0{:02d}x".format(site) + Device_name + "x{:02d}xTP25.txt".format(iter)
        print(flname)
          #      path = 'C:\\Users\\Username\\Path\\To\\File'
        with open( fullmap_point_data_path + flname) as f:

  #      with open( "C:/All_projects/tc18d_model_assessment/Data/correct/ESD_all_correct/Point_data/M008/" + flname) as f:
            lines_after_17=[]
            clean_lines=[]
            lines_after_17 = f.readlines()[46:70]
              #      print(lines_after_17)
            clean_lines = [x.strip(' ') for x in lines_after_17]
                #    print(clean_lines)


            for row in clean_lines:
                row = re.split(' +', row)
                        # row = row.split('/s* ')
                   #     print(row)
                Vgs.append(row[8])
                Ids.append(row[15])
                x = np.array(Vgs)
                y = np.array(Ids)
                 #       print(x)
                 #       print(y)


     #       continue
     #   else:
      #      continue

    #print(x)
    #print(y)
    print(Vgs)
    print(Ids)
    length_of_Vgs=len(Vgs)
    length_of_Ids=len(Ids)
    Vd=[]
    Vg=[]
    Idlin=[]
    Idsat=[]

    print(Ids[0])
    print(Ids[4])
    print(Ids[8])
    print(Ids[12])
    print(Ids[16])
    print(Ids[20])



    print(length_of_Vgs)
    #Vg=Vgs[0]
    #Idlin=Ids[0]

    print(Vg)
    print(Idlin)

    for j in range(0,length_of_Vgs):
        if j % 4 == 0:
            Vg.append(Vgs[j])

    for i in range(0,length_of_Ids):
        if i % 4 == 0:
            Idlin.append(Ids[i])
            Idsat.append(Ids[i+2])









        #    Vg = Vgs[j]



    print(Vg)
    print(Idlin)
    print(Idsat)


    x = [1.67730e-03,1.60140e-03,1.60960e-03,1.58380e-03,1.64970e-03]
    y = [9.92410e-03,9.54660e-03,9.57090e-03,9.49610e-03,9.90710e-03]

    print (x)

    print(y)


    Idlin2=list(map(float, Idlin))
    Idsat2=list(map(float, Idsat))

    Idlin_point_diff_Werner=[(x/Idlin_initial_meas_die20_werner3[iter-1]-1)*100 for x in Idlin2]
    Idsat_point_diff_Werner=[(x/Idsat_initial_meas_die20_werner3[iter-1]-1)*100 for x in Idsat2]


    print("Idlin_point_diff_Werner")
    print(Idlin_point_diff_Werner)

    print("Idsat_point_diff_Werner")
    print(Idsat_point_diff_Werner)
    die=[1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34,35,36,37,38,39]

    fig, bx = plt.subplots()

    bx.scatter(die, Idsat_point_diff_Werner, s=10, c='b', marker="s", label='point_fullmap')
    plt.grid(b=True, which='both', color='black', linestyle='-')

    plt.xlabel('Idsat_diff_Werner_die20(%)')
    plt.ylabel('Dies')
    picname= Device_name + "_{:02d}x_Idsat_difference_Werner.png".format(iter)
    plt.title(picname)


    plt.savefig(picname)



    plt.show()





    fig, cx = plt.subplots()

    cx.scatter(die, Idlin_point_diff_Werner, s=10, c='b', marker="s", label='point_fullmap')
    plt.grid(b=True, which='both', color='black', linestyle='-')

    plt.xlabel('Idlin_diff_Werner_die20(%)')
    plt.ylabel('Dies')
    picname=Device_name + "_{:02d}x_Idlin_difference_Werner.png".format(iter)
    plt.title(picname)

    plt.savefig(picname)



    plt.show()



## Idlin & Idsat vs Dies

    fig, dx = plt.subplots()

    dx.scatter(die, Idsat2, s=10, c='b', marker="s", label='point_fullmap')
    plt.grid(b=True, which='both', color='black', linestyle='-')

    plt.xlabel('Dies')
    plt.ylabel('Idsat_Dies')
    picname=Device_name + "_{:02d}x_Idsat_Dies.png".format(iter)
    plt.title(picname)


    plt.savefig(picname)



    plt.show()





    fig, ex = plt.subplots()

    ex.scatter(die, Idlin2, s=10, c='b', marker="s", label='point_fullmap')
    plt.grid(b=True, which='both', color='black', linestyle='-')

    plt.xlabel('Dies(%)')
    plt.ylabel('Idlin_Dies')
    picname=Device_name + "_{:02d}x_Idlin_Dies.png".format(iter)
    plt.title(picname)

    plt.savefig(picname)



    plt.show()





    pl.plot(Idlin_point_diff_Werner, Idsat_point_diff_Werner, "o")

    for x, y, z in zip(Idlin_point_diff_Werner, Idsat_point_diff_Werner, die):
        pl.text(x, y, str(z), color="red", fontsize=7)
    pl.margins(0.1)
    picname = Device_name + "_{:02d}x_Idlin-Idsat_percent_diff_to_werner.png".format(iter)
    pl.title(picname)
    pl.savefig(picname)




    pl.show()










    print(Idlin2)
    print(Idsat2)

    print (type(x))

    print (type(Idlin))

    fig, ax = plt.subplots()
    #ax.scatter(x, y)
    ax.scatter(Idlin2, Idsat2, s=10, c='b', marker="s", label='point_fullmap')
    ax.scatter(Idlin_initial_meas_die20_werner3[iter-1], Idsat_initial_meas_die20_werner3[iter-1], s=40, c='g', marker="*", label='Meas_initial_Die20')
  #  ax.scatter(Idlin_initial_red_die20, Idsat_initial_red_die20, s=20, c='c', marker="+", label='Meas_initial_Die20')
  #  ax.scatter(Idlin_initial_red_die21, Idsat_initial_red_die21, s=20, c='c', marker="+", label='Meas_initial_Die20')
  #  ax.scatter(Idlin_initial_red_die22, Idsat_initial_red_die22, s=20, c='c', marker="+", label='Meas_initial_Die20')
    ax.scatter(Idlin_initial_meas_die1_walter3[iter-1], Idsat_initial_meas_die1_walter3[iter-1], s=30, c='r', marker="D", label='Meas_initial_Die20')
    ax.scatter(Idlin_TT3[iter-1], Idsat_TT3[iter-1], s=70, c='lime', marker="D", label='Meas_initial_Die20')
    ax.scatter(Idlin_SS3[iter-1], Idsat_SS3[iter-1], s=70, c='lime', marker="D", label='Meas_initial_Die20')
    ax.scatter(Idlin_FF3[iter-1], Idsat_FF3[iter-1], s=70, c='lime', marker="D", label='Meas_initial_Die20')


    #plt.xlim(0.001, 0.0018)
    #plt.ylim(0.008, 0.0105)
    #ax.ticklabel_format(useOffset=False)
    plt.ticklabel_format(style='sci', axis='x', scilimits=(0.0005, 0.0098))
    plt.ticklabel_format(style='sci', axis='y', scilimits=(0.0005, 0.0405))


    plt.xlabel('Idlin(A)')
    plt.ylabel('Idsat(A)')

    if TYPE==-1:
        plt.gca().invert_yaxis()
        plt.gca().invert_xaxis()






   # plt.legend(["Point_measurement", "Remeas_Werner_die20", "Remeas_Werner_reduced_die20", "Remeas_Werner_reduced_die21", "Remeas_Werner_reduced_die22", "Remeas_Walter_die1"], loc="lower right")

    plt.legend(["Point_measurement", "Remeas_werner_die20", "Remeas_walter_die01" ,"Model-TT(contact res=2)"], loc="lower right")


    picname=Device_name + "_{:02d}xTP25.png".format(iter)
    plt.title(picname)


    plt.savefig(picname)
    plt.grid()
    plt.show()



    wb = xlwt.Workbook()
    ws = wb.add_sheet('Sheet 1')

    listdata = ['write', 'list', 'to', 'excel', 'row']

    first_row = 0
    second_row=1

    # write each item in the list to consecutive columns on the first row
    for index, item in enumerate(Idlin):
            ws.write(first_row, index, item)

    for index, item in enumerate(Idsat):
            ws.write(second_row, index, item)


    excelname=Device_name + "_{:02d}xTP25.png".format(iter)
    wb.save(excelname + '.xls')

