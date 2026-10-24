question="y"
total_hema=0
total_hemb=0
total_severe=0
total_moderate=0
total_mild=0

total_inhibitor_a=0
total_inhibitor_b=0
total_prophylaxis_a=0
total_prophylaxis_b=0
total_prop_moderate=0

total_plasma_a=0
total_plasma_b=0
total_recombinant_a=0
total_recombinant_b=0

total_plasma_f8_iu=0
total_plasma_f9_iu=0
total_recomb_f8_iu=0
total_recomb_f9_iu=0

totalvial_2000_p8=0
totalvial_1500_p8=0
totalvial_1000_p8=0
totalvial_500_p8=0
totalvial_250_p8=0

totalvial_2000_p9=0
totalvial_1500_p9=0
totalvial_1000_p9=0
totalvial_500_p9=0
totalvial_250_p9=0

totalvial_2000_r8=0
totalvial_1500_r8=0
totalvial_1000_r8=0
totalvial_500_r8=0
totalvial_250_r8=0

totalvial_2000_r9=0
totalvial_1500_r9=0
totalvial_1000_r9=0
totalvial_500_r9=0
totalvial_250_r9=0

totalcost_4weeks=0

max_amount_id_a=" "
max_amount_name_a=" "
max_amount_severity_a=" "
max_amount_weight_a=-1
max_amount_med_type_a=" "
max_amount_4weeks_iu_a=-1
max_amount_4weeks_cost_a=-1

max_amount_id_b=" "
max_amount_name_b=" "
max_amount_severity_b=" "
max_amount_weight_b=-1
max_amount_med_type_b=" "
max_amount_4weeks_iu_b=-1
max_amount_4weeks_cost_b=-1

max_cost_id=" "
max_cost_name=" "
max_cost_factor=0
max_cost_severity=" "
max_cost_weight=-1
max_cost_med_type=" "
max_cost_4weeks_iu=-1
max_cost_4weeks_cost=-1

while question=="Y" or question=="y":
    id=input("Enter ID ")
    name=input("Enter name and surname ")
    factor=int(input("Enter deficient factor protein(8/9) "))
    while factor!=8 and factor!=9:
        factor=int(input("Enter deficient factor protein(8/9) "))


    factor_level=float(input("Enter factor level (%) "))
    while factor_level<0 or factor_level>=50:
        factor_level=float(input("Enter factor level (%) "))

    bu=float(input("Enter antibody amount "))
    while bu<0:
        bu=float(input("Enter antibody amount "))

    if factor_level<1:
        severity="Severe"
        total_severe+=1
    elif factor_level<=5:
        severity="Moderate"
        total_moderate+=1
    else:
        severity="Mild"
        total_mild+=1
    if severity=="Moderate":
        bleeding_eps=int(input("Enter number of bleeding episodes in the past year "))
        while bleeding_eps<0:
            bleeding_eps=int(input("Enter number of bleeding episodes in the past year "))

    inhibitor=False
    if bu>=5:
        inhibitor=True
    
    prophylaxis=False
    if severity=="Severe" and inhibitor==False or severity=="Moderate" and inhibitor==False and bleeding_eps/12>=3:
        prophylaxis=True

    if prophylaxis:
        weight=float(input("Enter weight "))
        while weight<0:
            weight=float(input("Enter weight "))
        med_type=input("Enter medication type (Plasma-derived/Recombinant): (P/p/R/r) ")
        while med_type!="P" and med_type!="p" and med_type!="R" and med_type!="r":
            med_type=input("Enter medication type (Plasma-derived/Recombinant): (P/p/R/r) ")


    print(f"Patient's ID: {id}")
    print(f"Patient's name/surname: {name}")
    if factor==8:
        total_hema+=1
        print("Hemophilia type: A")
        if inhibitor:
            total_inhibitor_a+=1
    else:
        total_hemb+=1
        print("Hemophilia type: B")
        if inhibitor:
            total_inhibitor_b+=1


    print(f"Severity of disease: {severity}")
    
    if prophylaxis:
        print("Prophylaxis will be applied")
        if factor==8:
            total_prophylaxis_a+=1
            if med_type=="P" or med_type=="p":
                total_plasma_a+=1
            else:
                total_recombinant_a+=1
            print("Factor-8 will be used")
        else:
            total_prophylaxis_b+=1
            if med_type=="P" or med_type=="p":
                total_plasma_b+=1
            else:
                total_recombinant_b+=1
            print("Factor-9 will be used")
        if med_type=="P" or med_type=="p":
            print("Medication will be plasma-derived")
            med_type_formal="Plasma-derived"
        else:
            print("Medication will be recombinant")
            med_type_formal="Recombinant"
        if factor==8:
            print("Will be taken 3 times a week")
        else:
            print("Will be taken 2 times a week")
        
        if severity=="Moderate":
            total_prop_moderate+=1

        
        if factor==8:
            iu=(40-factor_level)/2*weight

        else:
            iu=(40-factor_level)*weight


        print(f"Minimum required dose of medication at one time: {iu:.2f} IU")

        temp_iu=iu
        vialnum_2000=0
        vialnum_1500=0
        vialnum_1000=0
        vialnum_500=0
        vialnum_250=0

        if temp_iu>=2000:
            vialnum_2000=temp_iu//2000
            temp_iu%=2000
        if temp_iu>1750:
            vialnum_2000+=1
            temp_iu=0
        if temp_iu>=1500:
            vialnum_1500=temp_iu//1500
            temp_iu%=1500
        if temp_iu>1250:
            vialnum_1500+=1
            temp_iu=0
        if temp_iu>=1000:
            vialnum_1000=temp_iu//1000
            temp_iu%=1000
        if temp_iu>750:
            vialnum_1000+=1
            temp_iu=0
        if temp_iu>=500:
            vialnum_500=temp_iu//500
            temp_iu%=500
        if temp_iu>250:
            vialnum_500+=1
            temp_iu=0
        if temp_iu>0 and temp_iu<=250:
            vialnum_250+=1
        
        given_med= int(vialnum_2000)*2000+int(vialnum_1500)*1500+int(vialnum_1000)*1000+int(vialnum_500)*500+vialnum_250*250

        print(f"Amount of medication to be used at one time: {given_med} IU")

        print(f"Number of 2000s vial needed: {int(vialnum_2000)}")
        print(f"Number of 1500s vial needed: {int(vialnum_1500)}")
        print(f"Number of 1000s vial needed: {int(vialnum_1000)}")
        print(f"Number of 500s vial needed: {int(vialnum_500)}")
        print(f"Number of 250s vial needed: {int(vialnum_250)}")
        
        if factor==8:
            given_med_4weeks=12*given_med
            print(f"Total amount of medication for 4 weeks: {given_med_4weeks} IU")

            if med_type=="P" or med_type=="p":
                total_plasma_f8_iu+=given_med_4weeks
            else:
                total_recomb_f8_iu+=given_med_4weeks

            if vialnum_2000!=0:
                vialnum_2000_4weeks=12*vialnum_2000
                print(f"Number of 2000s vial needed for 4 weeks: {int(vialnum_2000_4weeks)}")
                if med_type=="P" or med_type=="p":
                    totalvial_2000_p8+=vialnum_2000_4weeks
                else:
                    totalvial_2000_r8+=vialnum_2000_4weeks
            if vialnum_1500!=0:
                vialnum_1500_4weeks=12*vialnum_1500
                print(f"Number of 1500s vial needed for 4 weeks: {int(vialnum_1500_4weeks)}")
                if med_type=="P" or med_type=="p":
                    totalvial_1500_p8+=vialnum_1500_4weeks
                else:
                    totalvial_1500_r8+=vialnum_1500_4weeks
            if vialnum_1000!=0:
                vialnum_1000_4weeks=12*vialnum_1000
                print(f"Number of 1000s vial needed for 4 weeks: {int(vialnum_1000_4weeks)}")
                if med_type=="P" or med_type=="p":
                    totalvial_1000_p8+=vialnum_1000_4weeks
                else:
                    totalvial_1000_r8+=vialnum_1000_4weeks
            if vialnum_500!=0:
                vialnum_500_4weeks=12*vialnum_500
                print(f"Number of 500s vial needed for 4 weeks: {int(vialnum_500_4weeks)}")
                if med_type=="P" or med_type=="p":
                    totalvial_500_p8+=vialnum_500_4weeks
                else:
                    totalvial_500_r8+=vialnum_500_4weeks
            if vialnum_250!=0:
                vialnum_250_4weeks=12*vialnum_250
                print(f"Number of 250s vial needed for 4 weeks: {int(vialnum_250_4weeks)}")
                if med_type=="P" or med_type=="p":
                    totalvial_250_p8+=vialnum_250_4weeks
                else:
                    totalvial_250_r8+=vialnum_250_4weeks

        else:
            given_med_4weeks=8*given_med
            print(f"Total amount of medication for 4 weeks: {given_med_4weeks} IU")

            if med_type=="P" or med_type=="p":
                total_plasma_f9_iu+=given_med_4weeks
            else:
                total_recomb_f9_iu+=given_med_4weeks

            if vialnum_2000!=0:
                vialnum_2000_4weeks=8*vialnum_2000
                print(f"Number of 2000s vial needed for 4 weeks: {int(vialnum_2000_4weeks)}")
                if med_type=="P" or med_type=="p":
                    totalvial_2000_p9+=vialnum_2000_4weeks
                else:
                    totalvial_2000_r9+=vialnum_2000_4weeks
            if vialnum_1500!=0:
                vialnum_1500_4weeks=8*vialnum_1500
                print(f"Number of 1500s vial needed for 4 weeks: {int(vialnum_1500_4weeks)}")
                if med_type=="P" or med_type=="p":
                    totalvial_1500_p9+=vialnum_1500_4weeks
                else:
                    totalvial_1500_r9+=vialnum_1500_4weeks
            if vialnum_1000!=0:
                vialnum_1000_4weeks=8*vialnum_1000
                print(f"Number of 1000s vial needed for 4 weeks: {int(vialnum_1000_4weeks)}")
                if med_type=="P" or med_type=="p":
                    totalvial_1000_p9+=vialnum_1000_4weeks
                else:
                    totalvial_1000_r9+=vialnum_1000_4weeks
            if vialnum_500!=0:
                vialnum_500_4weeks=8*vialnum_500
                print(f"Number of 500s vial needed for 4 weeks: {int(vialnum_500_4weeks)}")
                if med_type=="P" or med_type=="p":
                    totalvial_500_p9+=vialnum_500_4weeks
                else:
                    totalvial_500_r9+=vialnum_500_4weeks
            if vialnum_250!=0:
                vialnum_250_4weeks=8*vialnum_250
                print(f"Number of 250s vial needed for 4 weeks: {int(vialnum_250_4weeks)}")
                if med_type=="P" or med_type=="p":
                    totalvial_250_p9+=vialnum_250_4weeks
                else:
                    totalvial_250_r9+=vialnum_250_4weeks
        
        if med_type=="P" or med_type=="p":
            cost_4weeks=0.3*given_med_4weeks
        else:
            cost_4weeks=0.4*given_med_4weeks
        print(f"Total medication cost for 4 weeks: ${cost_4weeks:.2f}")
        totalcost_4weeks+=cost_4weeks
        if factor==8:
            if given_med_4weeks>max_amount_4weeks_iu_a:
                max_amount_id_a=id
                max_amount_name_a=name
                max_amount_severity_a=severity
                max_amount_weight_a=weight
                max_amount_med_type_a=med_type_formal
                max_amount_4weeks_iu_a=given_med_4weeks
                max_amount_4weeks_cost_a=cost_4weeks
        else:
            if given_med_4weeks>max_amount_4weeks_iu_b:
                max_amount_id_b=id
                max_amount_name_b=name
                max_amount_severity_b=severity
                max_amount_weight_b=weight
                max_amount_med_type_b=med_type_formal
                max_amount_4weeks_iu_b=given_med_4weeks
                max_amount_4weeks_cost_b=cost_4weeks

        if cost_4weeks>max_cost_4weeks_cost:
            max_cost_id=id
            max_cost_name=name
            max_cost_factor=factor
            max_cost_severity=severity
            max_cost_weight=weight
            max_cost_med_type=med_type_formal
            max_cost_4weeks_iu=given_med_4weeks
            max_cost_4weeks_cost=cost_4weeks

    else:
        print("Prophylaxis won't be applied")

    question=input("Is there any more patient? (y/Y/n/N) ")
    while question!="Y" and question!="y" and question!="N" and question!="n":
        question=input("Is there any more patient? (y/Y/n/N) ")

total_patient=total_hema+total_hemb
severe_percentage=total_severe/total_patient*100
moderate_percentage=total_moderate/total_patient*100
mild_percentage=total_mild/total_patient*100

inhibitor_percentage_a=total_inhibitor_a/total_hema*100
inhibitor_percentage_b=total_inhibitor_b/total_hemb*100

prophylaxis_percentage_a=total_prophylaxis_a/total_hema*100
prophylaxis_percentage_b=total_prophylaxis_b/total_hemb*100

moderate_prop_percentage=total_prop_moderate/total_moderate*100
plasma_percentage_a=total_plasma_a/total_prophylaxis_a*100
plasma_percentage_b=total_plasma_b/total_prophylaxis_b*100
recombinant_percentage_a=total_recombinant_a/total_prophylaxis_a*100
recombinant_percentage_b=total_recombinant_b/total_prophylaxis_b*100

totalcost_yearly=totalcost_4weeks*13

total_annual_iu=(total_plasma_f8_iu + total_plasma_f9_iu + total_recomb_f8_iu + total_recomb_f9_iu)*13
total_prophylaxis=total_prophylaxis_a+total_prophylaxis_b

avr_annual_iu=total_annual_iu/total_prophylaxis
avr_annual_cost=totalcost_yearly/total_prophylaxis


print(f"Numbers of hemophilia-A: {total_hema}")
print(f"Numbers of hemophilia-B: {total_hemb}")
print(f"Numbers of patients: {total_patient}")
print(f"Numbers of patients with severe disease: {total_severe}")
print(f"Numbers of patients with moderate disease: {total_moderate}")
print(f"Numbers of patients with mild disease: {total_mild}")
print(f"Percentage of severe patients: %{severe_percentage:.2f}")
print(f"Percentage of moderate patients: %{moderate_percentage:.2f}")
print(f"Percentage of mild patients: %{mild_percentage:.2f}")

print(f"Percentages of inhibitor presence in Hemophilia-A: %{inhibitor_percentage_a:.2f}")
print(f"Percentages of inhibitor presence in Hemophilia-B: %{inhibitor_percentage_b:.2f}")
print(f"Numbers of patients receiving prophylaxis for Hemophilia-A: {total_prophylaxis_a}")
print(f"Percentage of patients receiving prophylaxis for Hemophilia-A: %{prophylaxis_percentage_a:.2f}")
print(f"Numbers of patients receiving prophylaxis for Hemophilia-B: {total_prophylaxis_b}")
print(f"Percentage of patients receiving prophylaxis for Hemophilia-B: %{prophylaxis_percentage_b:.2f}")
print(f"Percentage of patients receiving prophylaxis whose disease severity is moderate: %{moderate_prop_percentage:.2f}")

print(f"Percentage of patients using plasma-derived medications among Hemophilia-A receiving prophylaxis: %{plasma_percentage_a:.2f}")
print(f"Percentage of patients using recombinant medications among Hemophilia-A receiving prophylaxis: %{recombinant_percentage_a:.2f}")
print(f"Percentage of patients using plasma-derived medications among Hemophilia-B receiving prophylaxis: %{plasma_percentage_b:.2f}")
print(f"Percentage of patients using recombinant medications among Hemophilia-B receiving prophylaxis: %{recombinant_percentage_b:.2f}")

print(f"Total plasma-derived factor-8 for 4 weeks: {total_plasma_f8_iu} IU, number of 2000 IU: {int(totalvial_2000_p8)},",end=" ")
print(f"number of 1500 IU: {int(totalvial_1500_p8)}, number of 1000 IU: {int(totalvial_1000_p8)},",end=" ")
print(f"number of 500 IU: {int(totalvial_500_p8)}, number of 250 IU: {int(totalvial_250_p8)}")

print(f"Total recombinant factor-8 for 4 weeks: {total_recomb_f8_iu} IU, number of 2000 IU: {int(totalvial_2000_r8)},",end=" ")
print(f"number of 1500 IU: {int(totalvial_1500_r8)}, number of 1000 IU: {int(totalvial_1000_r8)},",end=" ")
print(f"number of 500 IU: {int(totalvial_500_r8)}, number of 250 IU: {int(totalvial_250_r8)}")

print(f"Total plasma-derived factor-9 for 4 weeks: {total_plasma_f9_iu} IU, number of 2000 IU: {int(totalvial_2000_p9)},",end=" ")
print(f"number of 1500 IU: {int(totalvial_1500_p9)}, number of 1000 IU: {int(totalvial_1000_p9)},",end=" ")
print(f"number of 500 IU: {int(totalvial_500_p9)}, number of 250 IU: {int(totalvial_250_p9)}")

print(f"Total recombinant factor-9 for 4 weeks: {total_recomb_f9_iu} IU, number of 2000 IU: {int(totalvial_2000_r9)},",end=" ")
print(f"number of 1500 IU: {int(totalvial_1500_r9)}, number of 1000 IU: {int(totalvial_1000_r9)},",end=" ")
print(f"number of 500 IU: {int(totalvial_500_r9)}, number of 250 IU: {int(totalvial_250_r9)}")

print(f"4-weeks factor medication costs for prophylaxis covered by the SSI: ${totalcost_4weeks:.2f}")
print(f"1-year factor medication costs for prophylaxis covered by the SSI: ${totalcost_yearly:.2f}")

print(f"Average annual total medication amount: {avr_annual_iu:.2f} IU")
print(f"Average annual total medication cost: ${avr_annual_cost:.2f}")

print(f"ID of Hemophilia-A patient with the highest 4-weeks medication amount: {max_amount_id_a}")
print(f"Name/Surname of Hemophilia-A patient with the highest 4-weeks medication amount: {max_amount_name_a}")
print(f"Severity of Hemophilia-A patient with the highest 4-weeks medication amount: {max_amount_severity_a}")
print(f"Weight of Hemophilia-A patient with the highest 4-weeks medication amount: {max_amount_weight_a:.2f}")
print(f"Medication type of Hemophilia-A patient with the highest 4-weeks medication amount: {max_amount_med_type_a}")
print(f"IU of Hemophilia-A patient with the highest 4-weeks medication amount: {max_amount_4weeks_iu_a} IU")
print(f"Cost of Hemophilia-A patient with the highest 4-weeks medication amount: ${max_amount_4weeks_cost_a:.2f}")

print(f"ID of Hemophilia-B patient with the highest 4-weeks medication amount: {max_amount_id_b}")
print(f"Name/Surname of Hemophilia-B patient with the highest 4-weeks medication amount: {max_amount_name_b}")
print(f"Severity of Hemophilia-B patient with the highest 4-weeks medication amount: {max_amount_severity_b}")
print(f"Weight of Hemophilia-B patient with the highest 4-weeks medication amount: {max_amount_weight_b:.2f}")
print(f"Medication type of Hemophilia-B patient with the highest 4-weeks medication amount: {max_amount_med_type_b}")
print(f"IU of Hemophilia-B patient with the highest 4-weeks medication amount: {max_amount_4weeks_iu_b} IU")
print(f"Cost of Hemophilia-B patient with the highest 4-weeks medication amount: ${max_amount_4weeks_cost_b:.2f}")

print(f"ID of patient with the highest 4-weeks medication cost: {max_cost_id}")
print(f"Name/Surname of patient with the highest 4-weeks medication cost: {max_cost_name}")
print(f"Type and severity of patient with the highest 4-weeks medication cost: Factor-{max_cost_factor}, {max_cost_severity}")
print(f"Weight of patient with the highest 4-weeks medication cost: {max_cost_weight:.2f}")
print(f"Medication type of patient with the highest 4-weeks medication cost: {max_cost_med_type}")
print(f"IU of patient with the highest 4-weeks medication cost: {max_cost_4weeks_iu} IU")
print(f"Cost of patient with the highest 4-weeks medication cost: ${max_cost_4weeks_cost:.2f}")
