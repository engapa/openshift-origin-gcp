# Copyright 2017 BBVA. All rights reserved.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

"""Creates the Compute Engine."""


def GenerateConfig(context):
  """Creates the Compute Engine with network and firewall."""

  resources = [{
      'name': context.env['deployment'] + '-dns',
      'type': 'dns.py',
      'properties': {
          'name': context.env['deployment'] + '-dns',
          'dns_name': context.properties['dns_name']
      }
  }, {
      'name': context.env['deployment'] + '-net',
      'type': 'network.py',
      'properties': {
          'name': context.env['deployment'] + '-net'
      }
  }, {
      'name': context.env['deployment'] + '-fw',
      'type': 'firewall.py',
      'properties': {
          'network': context.env['deployment'] + '-fw',
          'firewall_extra_ports': context.properties['firewall_extra_ports']
      }
  }]

  # for instance_group in context.properties['instances_groups']:
  #     resources.append(
  #         {
  #             'name': context.env['deployment'] + '-fw',
  #             'type': 'firewall.py',
  #             'properties': {
  #                 'network': context.env['deployment'] + '-fw',
  #                 'firewall_extra_ports': context.properties['firewall_extra_ports']
  #             }
  #         })

  net_output = [{'name': 'networkSelfLink',
              'value': '$(ref.' + resources[0]['name'] + '.selfLink)'}]

  dns_output = [{'name': 'dnsManagedZoneSelfLink',
              'value': '$(ref.' + resources[0]['name'] + '.selfLink)'}]

  return {'resources': resources, 'outputs': [net_output, dns_output]}