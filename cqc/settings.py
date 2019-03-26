#
# Copyright (c) 2017, Stephanie Wehner and Axel Dahlberg
# All rights reserved.
#
# Redistribution and use in source and binary forms, with or without
# modification, are permitted provided that the following conditions are met:
# 1. Redistributions of source code must retain the above copyright
#    notice, this list of conditions and the following disclaimer.
# 2. Redistributions in binary form must reproduce the above copyright
#    notice, this list of conditions and the following disclaimer in the
#    documentation and/or other materials provided with the distribution.
# 3. All advertising materials mentioning features or use of this software
#    must display the following acknowledgement:
#    This product includes software developed by Stephanie Wehner, QuTech.
# 4. Neither the name of the QuTech organization nor the
#    names of its contributors may be used to endorse or promote products
#    derived from this software without specific prior written permission.
#
# THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDER ''AS IS'' AND ANY
# EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT LIMITED TO, THE IMPLIED
# WARRANTIES OF MERCHANTABILITY AND FITNESS FOR A PARTICULAR PURPOSE ARE
# DISCLAIMED. IN NO EVENT SHALL THE COPYRIGHT HOLDER BE LIABLE FOR ANY
# DIRECT, INDIRECT, INCIDENTAL, SPECIAL, EXEMPLARY, OR CONSEQUENTIAL DAMAGES
# (INCLUDING, BUT NOT LIMITED TO, PROCUREMENT OF SUBSTITUTE GOODS OR SERVICES
# LOSS OF USE, DATA, OR PROFITS OR BUSINESS INTERRUPTION) HOWEVER CAUSED AND
# ON ANY THEORY OF LIABILITY, WHETHER IN CONTRACT, STRICT LIABILITY, OR TORT
# (INCLUDING NEGLIGENCE OR OTHERWISE) ARISING IN ANY WAY OUT OF THE USE OF THIS
# SOFTWARE, EVEN IF ADVISED OF THE POSSIBILITY OF SUCH DAMAGE.

import os
import logging
from configparser import ConfigParser


def get_config():
    """
    Returns the config of cqc
    :return: :obj: configparser.ConfigParser
    """
    config = ConfigParser()
    path_to_here = os.path.dirname(os.path.abspath(__file__))
    settings_file = os.path.join(path_to_here, "settings.ini")
    config.read(settings_file)
    return config


def set_config(config):
    """
    Sets the config of cqc
    :param config: :obj: configparser.ConfigParser
    :return: None
    """
    path_to_here = os.path.dirname(os.path.abspath(__file__))
    settings_file = os.path.join(path_to_here, "settings.ini")
    with open(settings_file, 'w') as f:
        config.write(f)


############################
# CONFIGURATION FILE FOR CQC
############################
config = get_config()

# The path to the file specifying the addresses and ports of the CQC nodes
# and the APP nodes.
# If using SimulaQron, this will be set by SimulaQron.
# Otherwise, specify the path to the files in the file settings.ini
CQC_CONF_CQC_FILE = config['FILEPATHS']['cqc_file']
CQC_CONF_APP_FILE = config['FILEPATHS']['app_file']

log_levels = {
    "info": logging.INFO,
    "debug": logging.DEBUG,
    "warning": logging.WARNING,
    "error": logging.ERROR,
    "critical": logging.CRITICAL
}
CQC_CONF_LOG_LEVEL = log_levels[config['LOGGING']['level']]

# Sets the time to wait between attempts to setup the connections to the cqc node
CQC_CONF_LINK_WAIT_TIME = float(config['WAITTIMES']['link_wait_time'])

# Sets the time to wait between attempts to setup the connections to other nodes for classical communication
CQC_CONF_COM_WAIT_TIME = float(config['WAITTIMES']['com_wait_time'])
