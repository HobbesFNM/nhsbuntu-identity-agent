import gi
gi.require_version('Gtk', '3.0')
from gi.repository import Gtk


"""
Hacky class to produce a PIN dialog window
"""
class PinDialog(Gtk.Window):

    def __init__(self, parent):
        Gtk.Window.__init__(self, title="Enter SmartCard PIN")
        box = Gtk.Box(orientation=Gtk.Orientation.VERTICAL, spacing=10)
        self.set_keep_above(True)
        self.add(box)
        self.set_border_width(10)
        labelbox = Gtk.Box(spacing=10)
        entrybox = Gtk.Box(spacing=5)
        msgbox = Gtk.Box(orientation=Gtk.Orientation.VERTICAL, spacing=5)
        buttonbox = Gtk.Box(spacing=5)

        box.pack_start(labelbox, True, True, 10)
        box.pack_start(entrybox, True, True, 0)
        box.pack_start(msgbox, True, True, 20)
        box.pack_start(buttonbox, True, True, 0)

        image = Gtk.Image.new_from_file("nhsbuntu.png")
        labelbox.add(image)

        label = Gtk.Label("Log in with SmartCard")
        label2 = Gtk.Label("Enter your passcode...")
        label3 = Gtk.Label("By entering your passcode you confirm your acceptance")
        label4 = Gtk.Label("of the NHS Care Identity Sevice terms and conditions.")
        self.entry = Gtk.Entry()
        self.entry.set_text("")
        self.entry.set_visibility(False)
        entrybox.add(label2)
        entrybox.add(self.entry)
        msgbox.add(label3)
        msgbox.add(label4)

        self.ok = Gtk.Button("OK")
        buttonbox.add(self.ok)
        buttonbox.set_child_packing(self.ok, False, False, 0, Gtk.PackType.END)
        self.ok.set_property("width-request", 100)

        self.cancel = Gtk.Button("Cancel")
        buttonbox.add(self.cancel)
        buttonbox.set_child_packing(self.cancel, False, False, 0, Gtk.PackType.END)
        self.cancel.set_property("width-request", 100)

        self.show_all()

    def register_ok(self, func):
        self.ok.connect("clicked", func)

    def register_cancel(self, func):
        self.cancel.connect("clicked", func)

"""
Class for Role Selector Dialog
""" 
class RoleSelectDialog(Gtk.Window):
    def __init__(self, parent):
        Gtk.Window.__init__(self, title="Select Your Role")
        self.set_border_width(10)
        self.set_default_size(250,500)

        self.roles = []
        scrolled = Gtk.ScrolledWindow()
        scrolled.set_policy(Gtk.PolicyType.NEVER, Gtk.PolicyType.AUTOMATIC)
        buttonbox = Gtk.Box(spacing=5)        
 
        box_outer = Gtk.Box(orientation=Gtk.Orientation.VERTICAL, spacing=10)
        box_outer.pack_start(scrolled, True, True, 0)
        box_outer.pack_start(buttonbox, False, False, 0)
        self.add(box_outer)

        self.listbox = Gtk.ListBox()
        #self.listbox.set_selection_mode(Gtk.SelectionMode.NONE)
        scrolled.add(self.listbox)
        #self.listbox.connect('row-activated', lambda widget, row: widget.role_id = row.data)

        #box_outer.pack_start(buttonbox, True, True, 0)

        self.ok = Gtk.Button("OK")
        buttonbox.add(self.ok)
        buttonbox.set_child_packing(self.ok, False, False, 0, Gtk.PackType.END)
        self.ok.set_property("width-request", 100)

        self.cancel = Gtk.Button("Cancel")
        buttonbox.add(self.cancel)
        buttonbox.set_child_packing(self.cancel, False, False, 0, Gtk.PackType.END)
        self.cancel.set_property("width-request", 100)

    def register_ok(self, func):
        self.ok.connect("clicked", func)

    def register_cancel(self, func):
        self.cancel.connect("clicked", func)


    def add_roles(self, roles):
        self.roles = roles
        for role in roles:
            self._add_role_to_listbox(role["org_name"] + " : " + 
                                      role["org_code"] + " : " + 
                                      role["name"], role["id"])

    def _add_role_to_listbox(self, role, role_id):
        row = Gtk.ListBoxRow()
        hbox = Gtk.Box(orientation=Gtk.Orientation.HORIZONTAL, spacing=10)
        label = Gtk.Label(role)
        hbox.pack_start(label, False, False, 0)
        hbox.set_border_width(10)
        row.add(hbox)
        row.data = role_id
        self.listbox.add(row)

"""
Tiny main window - required as hack to allow quitting the IA given we can't use an 
app indicator.

TODO Need to work out how to make it work in gnome shell without this
"""
class MainWindow(Gtk.Window):

    def __init__(self):
        Gtk.Window.__init__(self, title="NHSD Identity Agent")
        self.set_icon_from_file("ia.svg")
        self.set_default_size(250,0)
        self.set_border_width(0)


if __name__ == "__main__":
   response = {'cn': 'RA_A00394 RA A', 'sso_logout_url': 'https://gas.nis1.national.ncrs.nhs.uk/login/authlogout', 'roles': [{'org_name': 'STIRLING MEDICAL CENTRE (S KUMAR)', 'name': 'Demographic Administrator', 'org_code': 'B81012', 'id': '887389426511', 'sub_type': 'Admin', 'type': ' "Admin & Clerical'}, {'org_name': 'STIRLING MEDICAL CENTRE (S KUMAR)', 'name': 'Registration Authority Manager', 'org_code': 'B81012', 'id': '555008642106', 'sub_type': 'Management - A & C', 'type': ' "Admin & Clerical'}, {'org_name': 'PELHAM MEDICAL GROUP', 'name': 'Registration Authority Agent', 'org_code': 'B81016', 'id': '102048848984', 'sub_type': 'Admin', 'type': ' "Admin & Clerical'}, {'org_name': 'SAHA SN & DE G', 'name': 'Registration Authority Agent', 'org_code': 'B81108', 'id': '102048850986', 'sub_type': 'Admin', 'type': ' "Admin & Clerical'}, {'org_name': 'ASHWOOD SURGERY', 'name': 'Registration Authority Agent', 'org_code': 'B81603', 'id': '102048852982', 'sub_type': 'Admin', 'type': ' "Admin & Clerical'}, {'org_name': 'ASHWOOD SURGERY', 'name': 'Demographic Administrator', 'org_code': 'B81603', 'id': '107620875545', 'sub_type': 'Admin', 'type': ' "Admin & Clerical'}, {'org_name': 'STIRLING MEDICAL CENTRE (SINGH)', 'name': 'Registration Authority Agent', 'org_code': 'B81606', 'id': '102048854989', 'sub_type': 'Admin', 'type': ' "Admin & Clerical'}, {'org_name': 'GRASSINGTON MEDICAL CENTRE', 'name': 'Registration Authority Agent', 'org_code': 'B82099', 'id': '102048856985', 'sub_type': 'Admin', 'type': ' "Admin & Clerical'}, {'org_name': 'AMPLEFORTH SURGERY', 'name': 'Registration Authority Agent', 'org_code': 'B82609', 'id': '102048858981', 'sub_type': 'Admin', 'type': ' "Admin & Clerical'}, {'org_name': 'PEASHOLM SURGERY', 'name': 'Registration Authority Agent', 'org_code': 'B82611', 'id': '102048861981', 'sub_type': 'Admin', 'type': ' "Admin & Clerical'}, {'org_name': "DR K HICKEY'S PRACTICE", 'name': 'Registration Authority Agent', 'org_code': 'B83001', 'id': '102048864986', 'sub_type': 'Admin', 'type': ' "Admin & Clerical'}, {'org_name': 'CHARNWOOD SURGERY', 'name': 'Registration Authority Agent', 'org_code': 'C81006', 'id': '102048866982', 'sub_type': 'Admin', 'type': ' "Admin & Clerical'}, {'org_name': 'GRIMSTON MEDICAL CENTRE', 'name': 'Registration Authority Agent', 'org_code': 'D82010', 'id': '102048868989', 'sub_type': 'Admin', 'type': ' "Admin & Clerical'}, {'org_name': 'BRIDGE STREET SURGERY', 'name': 'Registration Authority Agent', 'org_code': 'D82015', 'id': '102048870980', 'sub_type': 'Admin', 'type': ' "Admin & Clerical'}, {'org_name': 'HUNSTANTON SURGERY', 'name': 'Registration Authority Agent', 'org_code': 'D82021', 'id': '102048872987', 'sub_type': 'Admin', 'type': ' "Admin & Clerical'}, {'org_name': 'HEACHAM GROUP SURGERY', 'name': 'Registration Authority Agent', 'org_code': 'D82027', 'id': '102048874983', 'sub_type': 'Admin', 'type': ' "Admin & Clerical'}, {'org_name': 'SOUTHGATES', 'name': 'Registration Authority Agent', 'org_code': 'D82099', 'id': '102048877988', 'sub_type': 'Admin', 'type': ' "Admin & Clerical'}, {'org_name': "ST CLEMENT'S SURGERY", 'name': 'Registration Authority Agent', 'org_code': 'D82105', 'id': '102048879984', 'sub_type': 'Admin', 'type': ' "Admin & Clerical'}, {'org_name': 'THE PRINCESS ROYAL HOSPITAL NHS TRUST', 'name': 'Registration Authority Agent', 'org_code': 'RKF', 'id': '102048881986', 'sub_type': 'Admin', 'type': ' "Admin & Clerical'}, {'org_name': 'VEDUTLA RDP', 'name': 'Registration Authority Agent', 'org_code': 'Y00221', 'id': '102048883982', 'sub_type': 'Admin', 'type': ' "Admin & Clerical'}, {'org_name': 'OPHTHALMOLOGY', 'name': 'Registration Authority Agent', 'org_code': 'Y00452', 'id': '102048885989', 'sub_type': 'Admin', 'type': ' "Admin & Clerical'}, {'org_name': 'NELPCT OUT OF HOURS SERVICE', 'name': 'Registration Authority Agent', 'org_code': 'Y00483', 'id': '102048887985', 'sub_type': 'Admin', 'type': ' "Admin & Clerical'}, {'org_name': 'KING STREET PHARMACY', 'name': 'Registration Authority Agent', 'org_code': 'FA079', 'id': '102054174981', 'sub_type': 'Admin', 'type': ' "Admin & Clerical'}, {'org_name': 'NORTH EAST LINCOLNSHIRE PCT', 'name': 'Demographic Administrator', 'org_code': '5AN', 'id': '905002982510', 'sub_type': 'Admin', 'type': ' "Admin & Clerical'}, {'org_name': 'WEST NORFOLK PCT', 'name': 'Demographic Administrator', 'org_code': '5CY', 'id': '384817818519', 'sub_type': 'Admin', 'type': ' "Admin & Clerical'}, {'org_name': 'COMMUNITY HEALTHCARE BOLTON NHS TRUST', 'name': 'Registration Authority Agent', 'org_code': 'RMM', 'id': '404523906513', 'sub_type': 'Admin', 'type': ' "Admin & Clerical'}, {'org_name': 'SOUTH TEES HOSPITALS NHS TRUST', 'name': 'Registration Authority Agent', 'org_code': 'RCJ', 'id': '880415398515', 'sub_type': 'Admin', 'type': ' "Admin & Clerical'}, {'org_name': 'DERMATOLOGY CLINIC', 'name': 'Registration Authority Agent', 'org_code': 'Y00167', 'id': '555006762108', 'sub_type': 'Admin', 'type': ' "Admin & Clerical'}, {'org_name': 'GLADSTONE HOUSE SURGERY', 'name': 'Registration Authority Agent', 'org_code': 'C81115', 'id': '555006782102', 'sub_type': 'Admin', 'type': ' "Admin & Clerical'}, {'org_name': 'GP PRACTICE EMIS CG001 001', 'name': 'Registration Authority Agent', 'org_code': 'A20074', 'id': '555006859104', 'sub_type': 'Admin', 'type': ' "Admin & Clerical'}, {'org_name': 'GP PRACTICE EMIS CG003 001', 'name': 'Registration Authority Agent', 'org_code': 'A20079', 'id': '555006863100', 'sub_type': 'Admin', 'type': ' "Admin & Clerical'}, {'org_name': 'TWO SHIRES AMBULANCE NHS TRUST', 'name': 'Registration Authority Agent', 'org_code': 'RHY', 'id': '555012026108', 'sub_type': 'Admin', 'type': ' "Admin & Clerical'}, {'org_name': 'SOUTH MOLTON HEALTH CENTRE', 'name': 'Registration Authority Agent', 'org_code': 'L83137', 'id': '555048763107', 'sub_type': 'Admin', 'type': ' "Admin & Clerical'}, {'org_name': 'ANCOATS PRIMARY CARE CENTRE', 'name': 'Registration Authority Agent', 'org_code': 'P84064', 'id': '555048767101', 'sub_type': 'Admin', 'type': ' "Admin & Clerical'}, {'org_name': 'GROVE SURGERY', 'name': 'Registration Authority Agent', 'org_code': 'J81646', 'id': '555048771107', 'sub_type': 'Admin', 'type': ' "Admin & Clerical'}, {'org_name': 'LEEN VIEW SURGERY', 'name': 'Registration Authority Agent', 'org_code': 'C84043', 'id': '555050250101', 'sub_type': 'Admin', 'type': ' "Admin & Clerical'}, {'org_name': "DR GI JONES' PRACTICE", 'name': 'Registration Authority Agent', 'org_code': 'C81611', 'id': '555050252103', 'sub_type': 'Admin', 'type': ' "Admin & Clerical'}, {'org_name': 'DR BOULTON AND PARTNERS', 'name': 'Registration Authority Agent', 'org_code': 'B85036', 'id': '555050254105', 'sub_type': 'Admin', 'type': ' "Admin & Clerical'}, {'org_name': 'PARK LANE SURGERY', 'name': 'Registration Authority Agent', 'org_code': 'C81040', 'id': '555052310107', 'sub_type': 'Admin', 'type': ' "Admin & Clerical'}, {'org_name': 'ST CLEMENTS HEALTH CENTRE', 'name': 'Registration Authority Agent', 'org_code': 'Y00999', 'id': '555055071105', 'sub_type': 'Admin', 'type': ' "Admin & Clerical'}], 'sso_ticket': 'AQIC5wM2LY4SfcxLNhapPqGROhxPuydEy28fzHWvYLbtWes=@AAJTSQACMDE=#'}
   def quit(self, source):
       Gtk.main_quit()
   m = MainWindow()
   rs = RoleSelectDialog(m)
   rs.add_roles(response["roles"])
   m.show_all()
   rs.show_all()
   rs.show()
   m.connect("delete-event", quit)
   Gtk.main()


