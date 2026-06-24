class SapAdapter:
    def __init__(self, session):
        # Get the SAP session initializted in main.py
        self.session = session

    def crear_orden_compra(self, oc):
        purchase_organization_code = oc.get_organization().get_purchase_organization_code() # PE 20
        organization_code = oc.get_organization().get_purchase_organization() # U03

        society_code = oc.get_organization().get_society_code() # PE 02
        caret_position_society_code = len(society_code)

        i = oc.get_service().get_i() # K
        p = oc.get_service().get_p() # F
        brief_description = oc.get_service().get_name() # SERV LUZ FEB 2026
        article_group = oc.get_service().get_article_group() # 03AD0104
        ce = oc.get_customer().get_sap_code() # P111

        applicant_code = str(oc.get_customer().get_applicant_code()).strip()
        caret_position_applicant_code = len(applicant_code)


        num_service = str(oc.get_service().get_num_service()) # 100024
        quantity = str(oc.get_service().get_quantity()) # 1
        caret_position_quantity = len(quantity)

        gross_price = str(oc.get_service().get_gross_price()) # 2265.18

    
        # BIEN
        name_provider = f"*{oc.get_provider().get_name().lower()}*"
        caret_position_name_provider = len(name_provider)
        provider_identifier = str(oc.get_provider().get_identifier()).strip() # 3000000625
        caret_position_provider_identifier = len(provider_identifier)

        row_information = f"OC {purchase_organization_code, organization_code, society_code} - Service: {i}, {p}, {brief_description}, {article_group}, {ce} - Provider ID: {provider_identifier} - Applicant Code: {applicant_code}, Quantity: {quantity}, Gross Price: {gross_price}, Name Provider: {name_provider}, Num Service: {num_service}, Name Provider: {name_provider}"
        print(f"🔍 Procesando: {row_information}")

        # Oc map
        try:
            # Block 1
            self.session.findById("wnd[0]").maximize()
            # Add to logic
            self.session.findById("wnd[0]/usr/subSUB0:SAPLMEGUI:0013/subSUB0:SAPLMEGUI:0030/subSUB1:SAPLMEGUI:1105/cmbMEPO_TOPLINE-BSART").key = "ZPLV"
            self.session.findById("wnd[0]/usr/subSUB0:SAPLMEGUI:0013/subSUB1:SAPLMEVIEWS:1100/subSUB2:SAPLMEVIEWS:1200/subSUB1:SAPLMEGUI:1102/tabsHEADER_DETAIL/tabpTABHDT9/ssubTABSTRIPCONTROL2SUB:SAPLMEGUI:1221/ctxtMEPO1222-EKORG").text = purchase_organization_code
            self.session.findById("wnd[0]/usr/subSUB0:SAPLMEGUI:0013/subSUB1:SAPLMEVIEWS:1100/subSUB2:SAPLMEVIEWS:1200/subSUB1:SAPLMEGUI:1102/tabsHEADER_DETAIL/tabpTABHDT9/ssubTABSTRIPCONTROL2SUB:SAPLMEGUI:1221/ctxtMEPO1222-EKGRP").text = organization_code
            self.session.findById("wnd[0]/usr/subSUB0:SAPLMEGUI:0013/subSUB1:SAPLMEVIEWS:1100/subSUB2:SAPLMEVIEWS:1200/subSUB1:SAPLMEGUI:1102/tabsHEADER_DETAIL/tabpTABHDT9/ssubTABSTRIPCONTROL2SUB:SAPLMEGUI:1221/ctxtMEPO1222-BUKRS").text = society_code

            # Pause
            self.session.findById("wnd[0]/usr/subSUB0:SAPLMEGUI:0013/subSUB1:SAPLMEVIEWS:1100/subSUB2:SAPLMEVIEWS:1200/subSUB1:SAPLMEGUI:1102/tabsHEADER_DETAIL/tabpTABHDT9/ssubTABSTRIPCONTROL2SUB:SAPLMEGUI:1221/ctxtMEPO1222-BUKRS").setFocus
            self.session.findById("wnd[0]/usr/subSUB0:SAPLMEGUI:0013/subSUB1:SAPLMEVIEWS:1100/subSUB2:SAPLMEVIEWS:1200/subSUB1:SAPLMEGUI:1102/tabsHEADER_DETAIL/tabpTABHDT9/ssubTABSTRIPCONTROL2SUB:SAPLMEGUI:1221/ctxtMEPO1222-BUKRS").caretPosition = caret_position_society_code
            self.session.findById("wnd[0]").sendVKey(27)
            

           # Block 2 USE THE FAST MODIFIER BUTTON
            tabla_id = "wnd[0]/usr/subSUB0:SAPLMEGUI:0013/subSUB2:SAPLMEVIEWS:1100/subSUB2:SAPLMEVIEWS:1200/subSUB1:SAPLMEGUI:1211/tblSAPLMEGUITC_1211"
            tabla = self.session.findById(tabla_id)

            # Ingreso de datos iniciales
            self.session.findById(f"{tabla_id}/ctxtMEPO1211-KNTTP[2,0]").text = i
            self.session.findById(f"{tabla_id}/ctxtMEPO1211-EPSTP[3,0]").text = p
            self.session.findById(f"{tabla_id}/txtMEPO1211-TXZ01[5,0]").text = brief_description
            self.session.findById(f"{tabla_id}/ctxtMEPO1211-WGBEZ[15,0]").text = article_group
            self.session.findById(f"{tabla_id}/ctxtMEPO1211-NAME1[16,0]").text = ce
            self.session.findById(f"{tabla_id}/ctxtMEPO1211-AFNAM[22,0]").text = applicant_code
            self.session.findById(f"{tabla_id}/ctxtMEPO1211-AFNAM[22,0]").setFocus()
            self.session.findById(f"{tabla_id}/ctxtMEPO1211-AFNAM[22,0]").caretPosition = caret_position_applicant_code

            # Proveedor
            self.session.findById("wnd[0]/usr/subSUB0:SAPLMEGUI:0013/subSUB0:SAPLMEGUI:0030/subSUB1:SAPLMEGUI:1105/ctxtMEPO_TOPLINE-SUPERFIELD").text = provider_identifier
            print("✅ provider_identifier OK: " + provider_identifier)

            self.session.findById("wnd[0]/usr/subSUB0:SAPLMEGUI:0013/subSUB0:SAPLMEGUI:0030/subSUB1:SAPLMEGUI:1105/ctxtMEPO_TOPLINE-SUPERFIELD").caretPosition = caret_position_provider_identifier
            self.session.findById("wnd[0]").sendVKey(0)

            superfield_value = self.session.findById("wnd[0]/usr/subSUB0:SAPLMEGUI:0019/subSUB0:SAPLMEGUI:0030/subSUB1:SAPLMEGUI:1105/ctxtMEPO_TOPLINE-SUPERFIELD").text
            print(f"DEBUG superfield: '{superfield_value}'")

            parts = superfield_value.strip().split(" ")
            provider_name_raw = parts[1] if len(parts) > 1 else ""
            name_provider = f"*{provider_name_raw.lower()}*"
            caret_position_name_provider = len(name_provider)

            print(f"DEBUG name_provider: '{name_provider}'")
            
            self.session.findById("wnd[0]/usr/subSUB0:SAPLMEGUI:0019/subSUB3:SAPLMEVIEWS:1100/subSUB2:SAPLMEVIEWS:1200/subSUB1:SAPLMEGUI:1301/subSUB2:SAPLMEGUI:1303/tabsITEM_DETAIL/tabpTABIDT1/ssubTABSTRIPCONTROL1SUB:SAPLMEGUI:1328/subSUB0:SAPLMLSP:0400/tblSAPLMLSPTC_VIEW/ctxtESLL-SRVPOS[2,0]").text = num_service
            print("✅ num_service OK: " + num_service)

            self.session.findById("wnd[0]/usr/subSUB0:SAPLMEGUI:0019/subSUB3:SAPLMEVIEWS:1100/subSUB2:SAPLMEVIEWS:1200/subSUB1:SAPLMEGUI:1301/subSUB2:SAPLMEGUI:1303/tabsITEM_DETAIL/tabpTABIDT1/ssubTABSTRIPCONTROL1SUB:SAPLMEGUI:1328/subSUB0:SAPLMLSP:0400/tblSAPLMLSPTC_VIEW/txtESLL-MENGE[4,0]").text = quantity
            print("✅ quantity OK: " + quantity)

            self.session.findById("wnd[0]/usr/subSUB0:SAPLMEGUI:0019/subSUB3:SAPLMEVIEWS:1100/subSUB2:SAPLMEVIEWS:1200/subSUB1:SAPLMEGUI:1301/subSUB2:SAPLMEGUI:1303/tabsITEM_DETAIL/tabpTABIDT1/ssubTABSTRIPCONTROL1SUB:SAPLMEGUI:1328/subSUB0:SAPLMLSP:0400/tblSAPLMLSPTC_VIEW/txtESLL-TBTWR[6,0]").text = gross_price
            print("✅ gross_price OK: " + gross_price)
            self.session.findById("wnd[0]/usr/subSUB0:SAPLMEGUI:0019/subSUB3:SAPLMEVIEWS:1100/subSUB2:SAPLMEVIEWS:1200/subSUB1:SAPLMEGUI:1301/subSUB2:SAPLMEGUI:1303/tabsITEM_DETAIL/tabpTABIDT1/ssubTABSTRIPCONTROL1SUB:SAPLMEGUI:1328/subSUB0:SAPLMLSP:0400/tblSAPLMLSPTC_VIEW/txtESLL-MENGE[4,0]").text = quantity
            self.session.findById("wnd[0]/usr/subSUB0:SAPLMEGUI:0019/subSUB3:SAPLMEVIEWS:1100/subSUB2:SAPLMEVIEWS:1200/subSUB1:SAPLMEGUI:1301/subSUB2:SAPLMEGUI:1303/tabsITEM_DETAIL/tabpTABIDT1/ssubTABSTRIPCONTROL1SUB:SAPLMEGUI:1328/subSUB0:SAPLMLSP:0400/tblSAPLMLSPTC_VIEW/txtESLL-MENGE[4,0]").caretPosition = caret_position_quantity
            print("✅ quantity OK: " + quantity)

            self.session.findById("wnd[0]").sendVKey(0)
            print("✅ sendVKey(0) después de quantity OK")

            self.session.findById("wnd[0]/usr/subSUB0:SAPLMEGUI:0019/subSUB3:SAPLMEVIEWS:1100/subSUB2:SAPLMEVIEWS:1200/subSUB1:SAPLMEGUI:1301/subSUB2:SAPLMEGUI:1303/tabsITEM_DETAIL/tabpTABIDT1/ssubTABSTRIPCONTROL1SUB:SAPLMEGUI:1328/subSUB0:SAPLMLSP:0400/tblSAPLMLSPTC_VIEW/txtESLL-TBTWR[6,0]").caretPosition = 6
            self.session.findById("wnd[1]").sendVKey(4)

            

            self.session.findById("wnd[2]/usr/tabsG_SELONETABSTRIP/tabpTAB001/ssubSUBSCR_PRESEL:SAPLSDH4:0220/sub:SAPLSDH4:0220/ctxtG_SELFLD_TAB-LOW[2,24]").text = society_code
            print("✅ society_code OK: " + society_code)


            self.session.findById("wnd[2]/usr/tabsG_SELONETABSTRIP/tabpTAB001/ssubSUBSCR_PRESEL:SAPLSDH4:0220/sub:SAPLSDH4:0220/txtG_SELFLD_TAB-LOW[6,24]").text = name_provider
            print("✅ name_provider OK: " + name_provider)

            self.session.findById("wnd[0]").sendVKey(0)
            self.session.findById("wnd[0]/usr/subSUB0:SAPLMEGUI:0019/subSUB3:SAPLMEVIEWS:1100/subSUB2:SAPLMEVIEWS:1200/subSUB1:SAPLMEGUI:1301/subSUB2:SAPLMEGUI:1303/tabsITEM_DETAIL/tabpTABIDT1/ssubTABSTRIPCONTROL1SUB:SAPLMEGUI:1328/subSUB0:SAPLMLSP:0400/tblSAPLMLSPTC_VIEW/txtESLL-TBTWR[6,0]").caretPosition = 6
            self.session.findById("wnd[0]").sendVKey(0)
            self.session.findById("wnd[0]").sendVKey(0)


            
        except Exception as e:
            print(f"❌ Error durante la ejecución en SAP: {e}")
            raise e