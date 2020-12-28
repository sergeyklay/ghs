# Copyright (C) 2020 Serghei Iakovlev <egrep@protonmail.ch>
#
# This file is free software; you can redistribute it and/or
# modify it under the terms of the GNU General Public License
# as published by the Free Software Foundation; either version 3
# of the License, or (at your option) any later version.
#
# This file is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this file.  If not, see <https://www.gnu.org/licenses/>.

import re


def get_error(ex) -> list:

    def replace(msg):
        wrp_regex = re.compile(r"(?:(?:std(?:out|err)|error):[ ]*'?|\n)")
        spc_regex = re.compile(r'[\s]{2,}')
        return spc_regex.sub(' ', wrp_regex.sub('', msg)).strip(" .'")

    holders = []

    if ex.stdout:
        holders.append(ex.stdout)
    if ex.stderr:
        holders.append(ex.stderr)

    messages = map(replace, holders)

    return list(messages)
