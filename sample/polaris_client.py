#! /usr/bin/env python3
import time
from timeit import default_timer as timer

import rubrik_polaris
import argparse
import pprint
from multiprocessing.pool import ThreadPool

pp = pprint.PrettyPrinter(indent=4)

parser = argparse.ArgumentParser()
parser.add_argument('-p', '--password', dest='password', help="Polaris Password", required=True)
parser.add_argument('-u', '--username', dest='username', help="Polaris UserName", required=True)
parser.add_argument('-d', '--domain', dest='domain', help="Polaris Domain", required=True)
parser.add_argument('-r', '--root', dest='root_domain', help="Polaris Root Domain", default=None)
parser.add_argument('--insecure', help='Deactivate SSL Verification', action="store_true")

args = parser.parse_args()

rubrik = rubrik_polaris.PolarisClient(args.domain, args.username, args.password, root_domain=args.root_domain,
                                      insecure=args.insecure)

# Add AWS Acct
# pp.pprint(rubrik.add_account_aws("789702809484", "peterm", ["us-east-1"]))
# Remove AWS Acct
# pp.pprint(rubrik.delete_account_aws())

# Run ODS for machines in a region using Gold retention, monitor to complete via threads
# on_demand_jobs=(rubrik.submit_on_demand(rubrik.get_object_ids_gce(region="us-west1"), rubrik.get_sla_domains(
# "Gold"), wait = True))
pp.pprint(rubrik.submit_on_demand(rubrik.get_object_ids_gce(region="us-west1"), rubrik.get_sla_domains(
    "Gold"), wait = True))

# pp.pprint(rubrik.get_accounts_aws_detail("789702809484"))
# pp.pprint(rubrik.get_sla_domains())
# pp.pprint(rubrik.get_sla_domains("Bronze"))
# pp.pprint(rubrik.get_accounts_aws("gurling"))
# pp.pprint(rubrik.get_accounts_gcp("Trinity-FDSE"))
# pp.pprint(rubrik.get_accounts_azure("RubrikRangers"))
# pp.pprint(rubrik.get_accounts_aws())
# pp.pprint(rubrik.get_accounts_gcp())
# pp.pprint(rubrik.get_accounts_azure())
# pp.pprint(rubrik.get_instances_ec2())
# pp.pprint(rubrik.get_instances_gce())
# pp.pprint(rubrik.get_instances_azure())


# pp.pprint(rubrik.submit_assign_sla( ["c0eb8a99-be0b-4122-a71e-4337fecddfb6"],"00000000-0000-0000-0000-000000000002" ))
# pp.pprint(rubrik.get_object_ids_ec2(tags = {"Name": "gurlingwinjb"}))
# pp.pprint(rubrik.get_object_ids_azure(region = "EastUS2"))
# pp.pprint(rubrik.get_object_ids_gce(region = "us-west1"))


