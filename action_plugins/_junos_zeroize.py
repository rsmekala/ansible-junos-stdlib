# -*- coding: utf-8 -*-

#
# Copyright (c) 2017-2018, Juniper Networks Inc. All rights reserved.
#
# License: Apache 2.0
#
# Redistribution and use in source and binary forms, with or without
# modification, are permitted provided that the following conditions are met:
#
# * Redistributions of source code must retain the above copyright
#   notice, this list of conditions and the following disclaimer.
#
# * Redistributions in binary form must reproduce the above copyright
#   notice, this list of conditions and the following disclaimer in the
#   documentation and/or other materials provided with the distribution.
#
# * Neither the name of the Juniper Networks nor the
#   names of its contributors may be used to endorse or promote products
#   derived from this software without specific prior written permission.
#
# THIS SOFTWARE IS PROVIDED BY Juniper Networks, Inc. ''AS IS'' AND ANY
# EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT LIMITED TO, THE IMPLIED
# WARRANTIES OF MERCHANTABILITY AND FITNESS FOR A PARTICULAR PURPOSE ARE
# DISCLAIMED. IN NO EVENT SHALL Juniper Networks, Inc. BE LIABLE FOR ANY
# DIRECT, INDIRECT, INCIDENTAL, SPECIAL, EXEMPLARY, OR CONSEQUENTIAL DAMAGES
# (INCLUDING, BUT NOT LIMITED TO, PROCUREMENT OF SUBSTITUTE GOODS OR SERVICES;
# LOSS OF USE, DATA, OR PROFITS; OR BUSINESS INTERRUPTION) HOWEVER CAUSED AND
# ON ANY THEORY OF LIABILITY, WHETHER IN CONTRACT, STRICT LIABILITY, OR TORT
# (INCLUDING NEGLIGENCE OR OTHERWISE) ARISING IN ANY WAY OUT OF THE USE OF THIS
# SOFTWARE, EVEN IF ADVISED OF THE POSSIBILITY OF SUCH DAMAGE.
#

from __future__ import absolute_import, division, print_function

# Standard library imports
import os.path
import sys

# From Ansible 2.1, Ansible uses Ansiballz for assembling modules
# Ansiballz packages module_utils into ansible.module_utils
from ansible.module_utils import juniper_junos_common


# Use the custom behavior of JuniperJunosActionModule as the superclass of
# our ActionModule.
class ActionModule(juniper_junos_common.JuniperJunosActionModule):
    """Translates junos_zeroize args to juniper_junos_system args.

    This class is a subclass of JuniperJunosActionModule. It exists solely
    for backwards compatibility. It translates the arguments from the old
    junos_zeroize module into the arguments on the new juniper_junos_system
    module.
    """
    def run(self, tmp=None, task_vars=None):
        # Check for the 'zeroize' option which was mandatory for
        # the junos_zeroize module.
        if 'zeroize' in self._task.args:
            # Delete the zeroize option.
            zeroize = self._task.args.pop('zeroize')
            # Add the action option with the value from the zeroize option.
            # This should normally be the value 'zeroize'. If it's not, then
            # the juniper_junos_system module will throw an appropriate error.
            self._task.args['action'] = zeroize

        # Remaining arguments can be passed through transparently.

        # Call the parent action module.
        return super(ActionModule, self).run(tmp, task_vars)
