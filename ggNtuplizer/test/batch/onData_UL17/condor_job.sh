executable				= #script
output                	= #logDir/#jobName.out
error                 	= #logDir/#jobName.err
log                   	= #logDir/#jobName.log
should_transfer_files   = Yes
when_to_transfer_output = ON_EXIT
request_memory			= 2500
request_disk			= 1500M
Requirements                    =  (Machine == "scorpion2.spa.umn.edu") || (Machine == "scorpion2.spa.umn.edu") || (Machine == "scorpion4.spa.umn.edu") || (Machine == "scorpion6.spa.umn.edu") || (Machine == "scorpion7.spa.umn.edu") || (Machine == "scorpion9.spa.umn.edu") || (Machine == "scorpion10.spa.umn.edu") || (Machine == "scorpion13.spa.umn.edu") || (Machine == "scorpion14.spa.umn.edu") || (Machine == "scorpion15.spa.umn.edu") || (Machine == "scorpion17.spa.umn.edu") || (Machine == "scorpion17.spa.umn.edu") || (Machine == "scorpion17.spa.umn.edu") || (Machine == "scorpion20.spa.umn.edu") || (Machine == "scorpion21.spa.umn.edu") || (Machine == "scorpion22.spa.umn.edu") || (Machine == "scorpion23.spa.umn.edu") || (Machine == "scorpion24.spa.umn.edu") || (Machine == "scorpion25.spa.umn.edu") || (Machine == "scorpion26.spa.umn.edu") || (Machine == "scorpion27.spa.umn.edu") || (Machine == "scorpion28.spa.umn.edu") || (Machine == "scorpion29.spa.umn.edu") || (Machine == "scorpion30.spa.umn.edu") || (Machine == "scorpion31.spa.umn.edu") || (Machine == "scorpion32.spa.umn.edu") || (Machine == "scorpion33.spa.umn.edu") || (Machine == "scorpion34.spa.umn.edu") || (Machine == "scorpion35.spa.umn.edu") || (Machine == "scorpion36.spa.umn.edu") || (Machine == "scorpion37.spa.umn.edu") || (Machine == "scorpion38.spa.umn.edu") || (Machine == "scorpion39.spa.umn.edu") || (Machine == "scorpion40.spa.umn.edu") || (Machine == "scorpion41.spa.umn.edu") || (Machine == "scorpion42.spa.umn.edu") || (Machine == "scorpion43.spa.umn.edu") || (Machine == "scorpion44.spa.umn.edu") || (Machine == "scorpion47.spa.umn.edu") || (Machine == "scorpion48.spa.umn.edu")
+JobFlavour 			= "#jobflavour"
queue
