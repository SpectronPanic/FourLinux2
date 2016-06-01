#!/usr/bin/python

import boto3

ec2 = boto3.resource("ec2")
client = boto3.client("ec2")

#instances = ec2.instances.filter(Filters=[{"Name":"instance-state-name","Values":["stopped"]}])
#for i in instances:
#    print(i.id, i.instance_type,i.network_interfaces)
#    print dir(i)
#    print i.key_pair

#for status in ec2.meta.client.describe_instance_status()['InstanceStatuses']:
#    print(status)

#print "Criando uma instancia"
#new_instance = ec2.create_instances(ImageId="ami-b2e3c6d8",MinCount=1,MaxCount=1,SecurityGroupIds=["sg-dc918cb6"])
#print new_instance
instance = ec2.instances.filter(InstanceIds=["i-c7b53844"])
sg = next( i for i in instance )
sg_py =  next(s for s in ec2.security_groups.all() if s.group_name == 'Python-SG')
print "Removendo grupo ",sg_py.group_id
#sg.security_groups.remove({"GroupName":sg_py.group_name,"GroupId":sg_py.group_id})
#instance = ec2.instances.filter(InstanceIds=["i-c7b53844"])
#sg = next( i for i in instance )
#print sg.security_groups
#sg = ec2.security_groups.all()
#for s in sg:
#    print s.group_name,s.group_id
#for i in instance:
#    print i.security_groups
#new_instance = ec2.instances.filter(InstanceIds=["i-e7ae2364"]).terminate()
#print new_instance
#vpc = ec2.Vpc.all()
#vpc = ec2.vpcs.all()
#for v in vpc:
#    print v.id
#for s in ec2.subnets.all():
#    print s

#print ec2.create_security_group(GroupName="Python-SG",Description="Grupo criado atraves do boto3")
sg = ec2.SecurityGroup("sg-dc918cb6")
#print sg.revoke_ingress(FromPort=80,ToPort=80,CidrIp="0.0.0.0/0",IpProtocol="tcp")
print sg.delete()


