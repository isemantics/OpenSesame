#-*- coding:utf-8 -*-

"""
This file is part of OpenSesame.

OpenSesame is free software: you can redistribute it and/or modify
it under the terms of the GNU General Public License as published by
the Free Software Foundation, either version 3 of the License, or
(at your option) any later version.

OpenSesame is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
GNU General Public License for more details.

You should have received a copy of the GNU General Public License
along with OpenSesame.  If not, see <http://www.gnu.org/licenses/>.
"""

from PyQt4 import QtGui
from libqtopensesame.extensions import base_extension

class quick_switcher(base_extension):

	"""
	desc:
		The quick-switcher allows you to quickly navigate to items and
		functions, and to quickly activate menu actions.
	"""

	def event_startup(self):

		"""
		desc:
			Initialize the quick_switcher.
		"""

		self.init_dialog()

	def event_open_experiment(self, path):

		"""
		desc:
			Re-init the dialog to update the recent files list.
		"""

		self.init_dialog()

	def init_dialog(self):

		"""
		desc:
			Re-init the dialog.
		"""

		from quick_switcher_dialog.dialog import quick_switcher
		self.d = quick_switcher(self.main_window)

	def activate(self):

		"""
		desc:
			Pops up the quick-switcher dialog.
		"""

		self.d.exec_()
