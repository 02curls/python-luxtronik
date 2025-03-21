"""Parse luxtronik calculations."""
import logging

from luxtronik.data_vector import DataVector

from luxtronik.datatypes import (
    BivalenceLevel,
    Bool,
    Celsius,
    Character,
    Count,
    Energy,
    Errorcode,
    Flow,
    Frequency,
    HeatpumpCode,
    Icon,
    IPv4Address,
    Kelvin,
    Level,
    MainMenuStatusLine1,
    MainMenuStatusLine2,
    MainMenuStatusLine3,
    OperationMode,
    Percent2,
    Power,
    Pressure,
    Seconds,
    SecOperationMode,
    Speed,
    SwitchoffFile,
    Timestamp,
    Unknown,
    MajorMinorVersion,
    Voltage,
)


class Calculations(DataVector):
    """Class that holds all calculations."""

    logger = logging.getLogger("Luxtronik.Calculations")
    name = "Calculation"

    def __init__(self):
        super().__init__()
        self._data = {
            0: Unknown("Unknown_Calculation_0"),
            1: Unknown("Unknown_Calculation_1"),
            2: Unknown("Unknown_Calculation_2"),
            3: Unknown("Unknown_Calculation_3"),
            4: Unknown("Unknown_Calculation_4"),
            5: Unknown("Unknown_Calculation_5"),
            6: Unknown("Unknown_Calculation_6"),
            7: Unknown("Unknown_Calculation_7"),
            8: Unknown("Unknown_Calculation_8"),
            9: Unknown("Unknown_Calculation_9"),
            10: Celsius("ID_WEB_Temperatur_TVL"),
            11: Celsius("ID_WEB_Temperatur_TRL"),
            12: Celsius("ID_WEB_Sollwert_TRL_HZ"),
            13: Celsius("ID_WEB_Temperatur_TRL_ext"),
            14: Celsius("ID_WEB_Temperatur_THG"),
            15: Celsius("ID_WEB_Temperatur_TA"),
            16: Celsius("ID_WEB_Mitteltemperatur"),
            17: Celsius("ID_WEB_Temperatur_TBW"),
            18: Celsius("ID_WEB_Einst_BWS_akt"),
            19: Celsius("ID_WEB_Temperatur_TWE"),
            20: Celsius("ID_WEB_Temperatur_TWA"),
            21: Celsius("ID_WEB_Temperatur_TFB1"),
            22: Celsius("ID_WEB_Sollwert_TVL_MK1"),
            23: Celsius("ID_WEB_Temperatur_RFV"),
            24: Celsius("ID_WEB_Temperatur_TFB2"),
            25: Celsius("ID_WEB_Sollwert_TVL_MK2"),
            26: Celsius("ID_WEB_Temperatur_TSK"),
            27: Celsius("ID_WEB_Temperatur_TSS"),
            28: Celsius("ID_WEB_Temperatur_TEE"),
            29: Bool("ID_WEB_ASDin"),
            30: Bool("ID_WEB_BWTin"),
            31: Bool("ID_WEB_EVUin"),
            32: Bool("ID_WEB_HDin"),
            33: Bool("ID_WEB_MOTin"),
            34: Bool("ID_WEB_NDin"),
            35: Bool("ID_WEB_PEXin"),
            36: Bool("ID_WEB_SWTin"),
            37: Bool("ID_WEB_AVout"),
            38: Bool("ID_WEB_BUPout"),
            39: Bool("ID_WEB_HUPout"),
            40: Bool("ID_WEB_MA1out"),
            41: Bool("ID_WEB_MZ1out"),
            42: Bool("ID_WEB_VENout"),
            43: Bool("ID_WEB_VBOout"),
            44: Bool("ID_WEB_VD1out"),
            45: Bool("ID_WEB_VD2out"),
            46: Bool("ID_WEB_ZIPout"),
            47: Bool("ID_WEB_ZUPout"),
            48: Bool("ID_WEB_ZW1out"),
            49: Bool("ID_WEB_ZW2SSTout"),
            50: Bool("ID_WEB_ZW3SSTout"),
            51: Bool("ID_WEB_FP2out"),
            52: Bool("ID_WEB_SLPout"),
            53: Bool("ID_WEB_SUPout"),
            54: Bool("ID_WEB_MZ2out"),
            55: Bool("ID_WEB_MA2out"),
            56: Seconds("ID_WEB_Zaehler_BetrZeitVD1"),
            57: Count("ID_WEB_Zaehler_BetrZeitImpVD1"),
            58: Seconds("ID_WEB_Zaehler_BetrZeitVD2"),
            59: Count("ID_WEB_Zaehler_BetrZeitImpVD2"),
            60: Seconds("ID_WEB_Zaehler_BetrZeitZWE1"),
            61: Seconds("ID_WEB_Zaehler_BetrZeitZWE2"),
            62: Seconds("ID_WEB_Zaehler_BetrZeitZWE3"),
            63: Seconds("ID_WEB_Zaehler_BetrZeitWP"),
            64: Seconds("ID_WEB_Zaehler_BetrZeitHz"),
            65: Seconds("ID_WEB_Zaehler_BetrZeitBW"),
            66: Seconds("ID_WEB_Zaehler_BetrZeitKue"),
            67: Seconds("ID_WEB_Time_WPein_akt"),
            68: Seconds("ID_WEB_Time_ZWE1_akt"),
            69: Seconds("ID_WEB_Time_ZWE2_akt"),
            70: Seconds("ID_WEB_Timer_EinschVerz"),
            71: Seconds("ID_WEB_Time_SSPAUS_akt"),
            72: Seconds("ID_WEB_Time_SSPEIN_akt"),
            73: Seconds("ID_WEB_Time_VDStd_akt"),
            74: Seconds("ID_WEB_Time_HRM_akt"),
            75: Seconds("ID_WEB_Time_HRW_akt"),
            76: Seconds("ID_WEB_Time_LGS_akt"),
            77: Seconds("ID_WEB_Time_SBW_akt"),
            78: HeatpumpCode("ID_WEB_Code_WP_akt"),
            79: BivalenceLevel("ID_WEB_BIV_Stufe_akt"),
            80: OperationMode("ID_WEB_WP_BZ_akt"),
            81: Character("ID_WEB_SoftStand_0"),
            82: Character("ID_WEB_SoftStand_1"),
            83: Character("ID_WEB_SoftStand_2"),
            84: Character("ID_WEB_SoftStand_3"),
            85: Character("ID_WEB_SoftStand_4"),
            86: Character("ID_WEB_SoftStand_5"),
            87: Character("ID_WEB_SoftStand_6"),
            88: Character("ID_WEB_SoftStand_7"),
            89: Character("ID_WEB_SoftStand_8"),
            90: Character("ID_WEB_SoftStand_9"),
            91: IPv4Address("ID_WEB_AdresseIP_akt"),
            92: IPv4Address("ID_WEB_SubNetMask_akt"),
            93: IPv4Address("ID_WEB_Add_Broadcast"),
            94: IPv4Address("ID_WEB_Add_StdGateway"),
            95: Timestamp("ID_WEB_ERROR_Time0"),
            96: Timestamp("ID_WEB_ERROR_Time1"),
            97: Timestamp("ID_WEB_ERROR_Time2"),
            98: Timestamp("ID_WEB_ERROR_Time3"),
            99: Timestamp("ID_WEB_ERROR_Time4"),
            100: Errorcode("ID_WEB_ERROR_Nr0"),
            101: Errorcode("ID_WEB_ERROR_Nr1"),
            102: Errorcode("ID_WEB_ERROR_Nr2"),
            103: Errorcode("ID_WEB_ERROR_Nr3"),
            104: Errorcode("ID_WEB_ERROR_Nr4"),
            105: Count("ID_WEB_AnzahlFehlerInSpeicher"),
            106: SwitchoffFile("ID_WEB_Switchoff_file_Nr0"),
            107: SwitchoffFile("ID_WEB_Switchoff_file_Nr1"),
            108: SwitchoffFile("ID_WEB_Switchoff_file_Nr2"),
            109: SwitchoffFile("ID_WEB_Switchoff_file_Nr3"),
            110: SwitchoffFile("ID_WEB_Switchoff_file_Nr4"),
            111: Timestamp("ID_WEB_Switchoff_file_Time0"),
            112: Timestamp("ID_WEB_Switchoff_file_Time1"),
            113: Timestamp("ID_WEB_Switchoff_file_Time2"),
            114: Timestamp("ID_WEB_Switchoff_file_Time3"),
            115: Timestamp("ID_WEB_Switchoff_file_Time4"),
            116: Bool("ID_WEB_Comfort_exists"),
            117: MainMenuStatusLine1("ID_WEB_HauptMenuStatus_Zeile1"),
            118: MainMenuStatusLine2("ID_WEB_HauptMenuStatus_Zeile2"),
            119: MainMenuStatusLine3("ID_WEB_HauptMenuStatus_Zeile3"),
            120: Seconds("ID_WEB_HauptMenuStatus_Zeit"),
            121: Level("ID_WEB_HauptMenuAHP_Stufe"),
            122: Celsius("ID_WEB_HauptMenuAHP_Temp"),
            123: Seconds("ID_WEB_HauptMenuAHP_Zeit"),
            124: Bool("ID_WEB_SH_BWW"),
            125: Icon("ID_WEB_SH_HZ"),
            126: Icon("ID_WEB_SH_MK1"),
            127: Icon("ID_WEB_SH_MK2"),
            128: Unknown("ID_WEB_Einst_Kurzrpgramm"),
            129: Unknown("ID_WEB_StatusSlave_1"),
            130: Unknown("ID_WEB_StatusSlave_2"),
            131: Unknown("ID_WEB_StatusSlave_3"),
            132: Unknown("ID_WEB_StatusSlave_4"),
            133: Unknown("ID_WEB_StatusSlave_5"),
            134: Timestamp("ID_WEB_AktuelleTimeStamp"),
            135: Icon("ID_WEB_SH_MK3"),
            136: Celsius("ID_WEB_Sollwert_TVL_MK3"),
            137: Celsius("ID_WEB_Temperatur_TFB3"),
            138: Bool("ID_WEB_MZ3out"),
            139: Bool("ID_WEB_MA3out"),
            140: Bool("ID_WEB_FP3out"),
            141: Seconds("ID_WEB_Time_AbtIn"),
            142: Celsius("ID_WEB_Temperatur_RFV2"),
            143: Celsius("ID_WEB_Temperatur_RFV3"),
            144: Icon("ID_WEB_SH_SW"),
            145: Unknown("ID_WEB_Zaehler_BetrZeitSW"),
            146: Bool("ID_WEB_FreigabKuehl"),
            147: Voltage("ID_WEB_AnalogIn"),
            148: Unknown("ID_WEB_SonderZeichen"),
            149: Icon("ID_WEB_SH_ZIP"),
            150: Icon("ID_WEB_WebsrvProgrammWerteBeobarten"),
            151: Energy("ID_WEB_WMZ_Heizung"),
            152: Energy("ID_WEB_WMZ_Brauchwasser"),
            153: Energy("ID_WEB_WMZ_Schwimmbad"),
            154: Energy("ID_WEB_WMZ_Seit"),
            155: Flow("ID_WEB_WMZ_Durchfluss"),
            156: Voltage("ID_WEB_AnalogOut1"),
            157: Voltage("ID_WEB_AnalogOut2"),
            158: Seconds("ID_WEB_Time_Heissgas"),
            159: Celsius("ID_WEB_Temp_Lueftung_Zuluft"),
            160: Celsius("ID_WEB_Temp_Lueftung_Abluft"),
            161: Seconds("ID_WEB_Zaehler_BetrZeitSolar"),
            162: Voltage("ID_WEB_AnalogOut3"),
            163: Voltage("ID_WEB_AnalogOut4"),
            164: Voltage("ID_WEB_Out_VZU"),
            165: Voltage("ID_WEB_Out_VAB"),
            166: Bool("ID_WEB_Out_VSK"),
            167: Bool("ID_WEB_Out_FRH"),
            168: Voltage("ID_WEB_AnalogIn2"),
            169: Voltage("ID_WEB_AnalogIn3"),
            170: Bool("ID_WEB_SAXin"),
            171: Bool("ID_WEB_SPLin"),
            172: Bool("ID_WEB_Compact_exists"),
            173: Flow("ID_WEB_Durchfluss_WQ"),
            174: Bool("ID_WEB_LIN_exists"),
            175: Celsius("ID_WEB_LIN_ANSAUG_VERDAMPFER"),
            176: Celsius("ID_WEB_LIN_ANSAUG_VERDICHTER"),
            177: Celsius("ID_WEB_LIN_VDH"),
            178: Kelvin("ID_WEB_LIN_UH"),
            179: Kelvin("ID_WEB_LIN_UH_Soll"),
            180: Pressure("ID_WEB_LIN_HD"),
            181: Pressure("ID_WEB_LIN_ND"),
            182: Bool("ID_WEB_LIN_VDH_out"),
            183: Percent2("ID_WEB_HZIO_PWM"),
            184: Speed("ID_WEB_HZIO_VEN"),
            185: Unknown("ID_WEB_HZIO_EVU2"),
            186: Bool("ID_WEB_HZIO_STB"),
            187: Energy("ID_WEB_SEC_Qh_Soll"),
            188: Energy("ID_WEB_SEC_Qh_Ist"),
            189: Celsius("ID_WEB_SEC_TVL_Soll"),
            190: Unknown("ID_WEB_SEC_Software"),
            191: SecOperationMode("ID_WEB_SEC_BZ"),
            192: Unknown("ID_WEB_SEC_VWV"),
            193: Speed("ID_WEB_SEC_VD"),
            194: Celsius("ID_WEB_SEC_VerdEVI"),
            195: Celsius("ID_WEB_SEC_AnsEVI"),
            196: Kelvin("ID_WEB_SEC_UEH_EVI"),
            197: Kelvin("ID_WEB_SEC_UEH_EVI_S"),
            198: Celsius("ID_WEB_SEC_KondTemp"),
            199: Celsius("ID_WEB_SEC_FlussigEx"),
            200: Celsius("ID_WEB_SEC_UK_EEV"),
            201: Pressure("ID_WEB_SEC_EVI_Druck"),
            202: Voltage("ID_WEB_SEC_U_Inv"),
            203: Celsius("ID_WEB_Temperatur_THG_2"),
            204: Celsius("ID_WEB_Temperatur_TWE_2"),
            205: Celsius("ID_WEB_LIN_ANSAUG_VERDAMPFER_2"),
            206: Celsius("ID_WEB_LIN_ANSAUG_VERDICHTER_2"),
            207: Celsius("ID_WEB_LIN_VDH_2"),
            208: Kelvin("ID_WEB_LIN_UH_2"),
            209: Kelvin("ID_WEB_LIN_UH_Soll_2"),
            210: Pressure("ID_WEB_LIN_HD_2"),
            211: Pressure("ID_WEB_LIN_ND_2"),
            212: Bool("ID_WEB_HDin_2"),
            213: Bool("ID_WEB_AVout_2"),
            214: Bool("ID_WEB_VBOout_2"),
            215: Bool("ID_WEB_VD1out_2"),
            216: Bool("ID_WEB_LIN_VDH_out_2"),
            217: SwitchoffFile("ID_WEB_Switchoff2_file_Nr0"),
            218: SwitchoffFile("ID_WEB_Switchoff2_file_Nr1"),
            219: SwitchoffFile("ID_WEB_Switchoff2_file_Nr2"),
            220: SwitchoffFile("ID_WEB_Switchoff2_file_Nr3"),
            221: SwitchoffFile("ID_WEB_Switchoff2_file_Nr4"),
            222: Timestamp("ID_WEB_Switchoff2_file_Time0"),
            223: Timestamp("ID_WEB_Switchoff2_file_Time1"),
            224: Timestamp("ID_WEB_Switchoff2_file_Time2"),
            225: Timestamp("ID_WEB_Switchoff2_file_Time3"),
            226: Timestamp("ID_WEB_Switchoff2_file_Time4"),
            227: Celsius("ID_WEB_RBE_RT_Ist"),
            228: Celsius("ID_WEB_RBE_RT_Soll"),
            229: Celsius("ID_WEB_Temperatur_BW_oben"),
            230: HeatpumpCode("ID_WEB_Code_WP_akt_2"),
            231: Frequency("ID_WEB_Freq_VD"),
            232: Celsius("Vapourisation_Temperature"),
            233: Celsius("Liquefaction_Temperature"),
            234: Unknown("Unknown_Calculation_234"),
            235: Unknown("Unknown_Calculation_235"),
            236: Frequency("ID_WEB_Freq_VD_Soll"),
            237: Frequency("ID_WEB_Freq_VD_Min"),
            238: Frequency("ID_WEB_Freq_VD_Max"),
            239: Kelvin("VBO_Temp_Spread_Soll"),
            240: Kelvin("VBO_Temp_Spread_Ist"),
            241: Percent2("HUP_PWM"),
            242: Kelvin("HUP_Temp_Spread_Soll"),
            243: Kelvin("HUP_Temp_Spread_Ist"),
            244: Unknown("Unknown_Calculation_244"),
            245: Unknown("Unknown_Calculation_245"),
            246: Unknown("Unknown_Calculation_246"),
            247: Unknown("Unknown_Calculation_247"),
            248: Unknown("Unknown_Calculation_248"),
            249: Unknown("Unknown_Calculation_249"),
            250: Unknown("Unknown_Calculation_250"),
            251: Unknown("Unknown_Calculation_251"),
            252: Unknown("Unknown_Calculation_252"),
            253: Unknown("Unknown_Calculation_253"),
            254: Flow("Flow_Rate_254"),
            255: Unknown("Unknown_Calculation_255"),
            256: Unknown("Unknown_Calculation_256"),
            257: Power("Heat_Output"),
            258: MajorMinorVersion("RBE_Version"),
            259: Unknown("Unknown_Calculation_259"),
        }
