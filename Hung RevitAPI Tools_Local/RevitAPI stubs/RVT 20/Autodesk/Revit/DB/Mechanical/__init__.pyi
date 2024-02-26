from typing import Tuple, Set, Iterable, List


class OccupancyUnit:
    NumberOfPeople = 0
    AreaPerPerson = 1
    BySpaceType = -1
    UseDefaultValues = -1


class DuctSystemType:
    UndefinedSystemType = 0
    SupplyAir = 1
    ReturnAir = 2
    ExhaustAir = 3
    OtherAir = 4
    Fitting = 28
    Global = 29


class SystemCalculationLevel:
    #None = 0
    Flow = 1
    Volume = 2
    Performance = 4
    All = -1


class RiseDropSymbol:
    NoSymbol = 0
    Outline = 1
    Cross = 2
    CrossFilled = 3
    Slash = 4
    SlashFilled = 5
    Backslash = 6
    BackslashFilled = 7
    Wye = 8
    ReverseWye = 9
    OutlineFilled = 10
    YinYang = 11
    YinYangFilled = 12
    BendThreeQuarterCircle = 13
    BendFullCircle = 14
    TeeHalfCircle = 15
    TeeFullCircle = 16
    CrossNoOutline = 17
    WyeFilled = 18
    ReverseWyeFilled = 19
    CustomSymbol = -1


class ReturnAirflowType:
    Specified = 0
    SpecifiedSupplyAirflow = 1
    CalculatedSupplyAirflow = 2
    ActualSupplyAirflow = 3


class ConditionType:
    Heated = 0
    Cooled = 1
    HeatedAndCooled = 2
    Unconditioned = 3
    Vented = 4
    NaturallyVentedOnly = 5
    NoOfConditionTypes = 6


class SpaceType:
    kActiveStorage = 0
    kActiveStorageHospitalOrHealthcare = 1
    kAirOrTrainOrBusBaggageArea = 2
    kAirportConcourse = 3
    kAtriumEachAdditionalFloor = 4
    kAtriumFirstThreeFloors = 5
    kAudienceOrSeatingAreaPenitentiary = 6
    kAudienceOrSeatingAreaExerciseCenter = 7
    kAudienceOrSeatingAreaGymnasium = 8
    kAudienceOrSeatingAreaSportsArena = 9
    kAudienceOrSeatingAreaConventionCenter = 10
    kAudienceOrSeatingAreaMotionPictureTheatre = 11
    kAudienceOrSeatingAreaPerformingArtsTheatre = 12
    kAudienceOrSeatingAreaReligious = 13
    kAudienceOrSeatingAreaPoliceOrFireStations = 14
    kAudienceOrSeatingAreaCourtHouse = 15
    kAudienceOrSeatingAreaAuditorium = 16
    kBankCustomerArea = 17
    kBankingActivityAreaOffice = 18
    kBarberAndBeautyParlor = 19
    kCardFileAndCataloguingLibrary = 20
    kClassroomOrLectureOrTrainingPenitentiary = 21
    kClassroomOrLectureOrTraining = 22
    kComfinementCellsPenitentiary = 23
    kComfinementCellsCourtHouse = 24
    kConferenceMeetingOrMultipurpose = 25
    kCorridorOrTransition = 26
    kCorridorOrTransitionManufacturingFacility = 27
    kCorridorsWithPatientWaitingExamHospitalOrHealthcare = 28
    kCourtSportsAreaSportsArena = 29
    kCourtroomCourtHouse = 30
    kDepartmentStoreSalesAreaRetail = 31
    kDetailedManufacturingFacility = 32
    kDiningArea = 33
    kDiningAreaHotel = 34
    kDiningAreaFamilyDining = 35
    kDiningAreaLoungeOrLeisureDining = 36
    kDiningAreaMotel = 37
    kDiningAreaTransportation = 38
    kDiningAreaPenitentiary = 39
    kDiningAreaCivilServices = 40
    kDormitoryBedroom = 41
    kDormitoryStudyHall = 42
    kDressingOrLockerOrFittingRoomGymnasium = 43
    kDressingOrLockerOrFittingRoomCourtHouse = 44
    kDressingOrLockerOrFittingRoomPerformingArtsTheatre = 45
    kDressingOrLockerOrFittingRoomAuditorium = 46
    kDressingOrLockerOrFittingRoomExerciseCenter = 47
    kElectricalOrMechanical = 48
    kElevatorLobbies = 49
    kEmergencyHospitalOrHealthcare = 50
    kEquipmentRoomManufacturingFacility = 51
    kExamOrTreatmentHospitalOrHealthcare = 52
    kExerciseAreaExerciseCenter = 53
    kExerciseAreaGymnasium = 54
    kExhibitSpaceConventionCenter = 55
    kFellowshipHallReligiousBuildings = 56
    kFineMaterialWarehouse = 57
    kFineMerchandiseSalesAreaRetail = 58
    kFireStationEngineRoomPoliceOrFireStation = 59
    kFoodPreparation = 60
    kGarageServiceOrRepairAutomotiveFacility = 61
    kGeneralHighBayManufacturingFacility = 62
    kGeneralLowBayManufacturingFacility = 63
    kGeneralExhibitionMuseum = 64
    kHospitalNurseryHospitalOrHealthcare = 65
    kHospitalOrMedicalSuppliesHospitalOrHealthcare = 66
    kHospitalOrRadiologyHospitalOrHealthcare = 67
    kHotelOrConferenceCenterConferenceOrMeeting = 68
    kInactiveStorage = 69
    kJudgesChambersCourtHouse = 70
    kLaboratoryOffice = 71
    kLaundryIroningAndSorting = 72
    kLaundryWashingHospitalOrHealthcare = 73
    kLibraryAudioVisualLibraryAudioVisual = 74
    kLivingQuartersDormitory = 75
    kLivingQuartersMotel = 76
    kLivingQuartersHotel = 77
    kLobby = 78
    kLobbyReligiousBuildings = 79
    kLobbyMotionPictureTheatre = 80
    kLobbyAuditorium = 81
    kLobbyPerformingArtsTheatre = 82
    kLobbyPostOffice = 83
    kLobbyHotel = 84
    kLoungeOrRecreation = 85
    kMallConcourseSalesAreaRetail = 86
    kMassMerchandisingSalesAreaRetail = 87
    kMediumOrBulkyMaterialWarehouse = 88
    kMerchandisingSalesAreaRetail = 89
    kMuseumAndGalleryStorage = 90
    kNurseStationHospitalOrHealthcare = 91
    kOfficeEnclosed = 92
    kOfficeOpenPlan = 93
    kOfficeCommonActivityAreasInactiveStorage = 94
    kOperatingRoomHospitalOrHealthcare = 95
    kOtherTelevisedPlayingAreaSportsArena = 96
    kParkingAreaAttendantOnlyParkingGarage = 97
    kParkingAreaPedestrianParkingGarage = 98
    kPatientRoomHospitalOrHealthcare = 99
    kPersonalServicesSalesAreaRetail = 100
    kPharmacyHospitalOrHealthcare = 101
    kPhysicalTherapyHospitalOrHealthcare = 102
    kPlayingAreaGymnasium = 103
    kPlenum = 104
    kPoliceStationLaboratoryPoliceOrFireStations = 105
    kPublicAndStaffLoungeHospitalOrHealthcare = 106
    kReadingAreaLibrary = 107
    kReceptionOrWaitingTransportation = 108
    kReceptionOrWaitingMotel = 109
    kReceptionOrWaitingHotel = 110
    kRecoveryHospitalOrHealthcare = 111
    kRestorationMuseum = 112
    kRestrooms = 113
    kRingSportsAreaSportsArena = 114
    kSleepingQuartersPoliceOrFireStation = 115
    kSortingAreaPostOffice = 116
    kSpecialtyStoreSalesAreaRetail = 117
    kStacksLibrary = 118
    kStairsInactive = 119
    kStairway = 120
    kSupermarketSalesAreaRetail = 121
    kTerminalTicketCounterTransportation = 122
    kWorkshopWorkshop = 123
    kWorshipPulpitChoirReligious = 124
    kNoOfSpaceTypes = 125
    NoSpaceType = -1


class DuctFlowConfigurationType:
    Calculated = 0
    Preset = 1
    System = 2


class DuctLossMethodType:
    NotDefined = 0
    SpecificLoss = 4
    Coefficient = 6


class SpaceSet(APIObject):
    def __init__(self): ...
    def Clear(self) -> None: ...
    @property
    def Size(self) -> int: ...
    @property
    def IsEmpty(self) -> bool: ...
    def ForwardIterator(self) -> SpaceSetIterator: ...
    def ReverseIterator(self) -> SpaceSetIterator: ...
    def GetEnumerator(self) -> IEnumerator: ...
    def Contains(self, item: Space) -> bool: ...
    def Insert(self, item: Space) -> bool: ...
    def Erase(self, item: Space) -> int: ...


class SpaceSetIterator(APIObject):
    def __init__(self): ...
    @property
    def Current(self) -> Object: ...
    def MoveNext(self) -> bool: ...
    def Reset(self) -> None: ...


class Space(SpatialElement):
    @property
    def Zone(self) -> Zone: ...
    @property
    def ClosedShell(self) -> GeometryElement: ...
    @property
    def Room(self) -> Room: ...
    @property
    def UpperLimit(self) -> Level: ...
    @UpperLimit.setter
    def UpperLimit(self, plev: Level) -> None: ...
    @property
    def LimitOffset(self) -> float: ...
    @LimitOffset.setter
    def LimitOffset(self, vLimitOffset: float) -> None: ...
    @property
    def BaseOffset(self) -> float: ...
    @BaseOffset.setter
    def BaseOffset(self, vBaseOffset: float) -> None: ...
    @property
    def AverageEstimatedIllumination(self) -> float: ...
    @property
    def SpaceCavityRatio(self) -> float: ...
    @property
    def LightingCalculationWorkplane(self) -> float: ...
    @LightingCalculationWorkplane.setter
    def LightingCalculationWorkplane(self, vLightingcw: float) -> None: ...
    @property
    def CeilingReflectance(self) -> float: ...
    @CeilingReflectance.setter
    def CeilingReflectance(self, vCeilingReflect: float) -> None: ...
    @property
    def WallReflectance(self) -> float: ...
    @WallReflectance.setter
    def WallReflectance(self, vWallReflect: float) -> None: ...
    @property
    def FloorReflectance(self) -> float: ...
    @FloorReflectance.setter
    def FloorReflectance(self, vFloorReflect: float) -> None: ...
    @property
    def DesignHVACLoadperArea(self) -> float: ...
    @DesignHVACLoadperArea.setter
    def DesignHVACLoadperArea(self, vDesignHVACLoadperArea: float) -> None: ...
    @property
    def ActualHVACLoad(self) -> float: ...
    @property
    def DesignOtherLoadperArea(self) -> float: ...
    @DesignOtherLoadperArea.setter
    def DesignOtherLoadperArea(self, vDesignOtherLoadperArea: float) -> None: ...
    @property
    def ActualOtherLoad(self) -> float: ...
    @property
    def DesignSupplyAirflow(self) -> float: ...
    @DesignSupplyAirflow.setter
    def DesignSupplyAirflow(self, vDesignSupplyAirflow: float) -> None: ...
    @property
    def CalculatedSupplyAirflow(self) -> float: ...
    @property
    def ActualSupplyAirflow(self) -> float: ...
    @property
    def ReturnAirflow(self) -> ReturnAirflowType: ...
    @ReturnAirflow.setter
    def ReturnAirflow(self, eReturnAirflow: ReturnAirflowType) -> None: ...
    @property
    def DesignReturnAirflow(self) -> float: ...
    @DesignReturnAirflow.setter
    def DesignReturnAirflow(self, vDesignReturnAirflow: float) -> None: ...
    @property
    def ActualReturnAirflow(self) -> float: ...
    @property
    def DesignExhaustAirflow(self) -> float: ...
    @DesignExhaustAirflow.setter
    def DesignExhaustAirflow(self, vDesignExhaustAirflow: float) -> None: ...
    @property
    def ActualExhaustAirflow(self) -> float: ...
    @property
    def OutdoorAirPerPerson(self) -> float: ...
    @property
    def OutdoorAirPerArea(self) -> float: ...
    @property
    def AirChangesPerHour(self) -> float: ...
    @property
    def OutdoorAirflow(self) -> float: ...
    @property
    def OutdoorAirFlowStandard(self) -> OutdoorAirFlowStandard: ...
    @property
    def UnboundedHeight(self) -> float: ...
    @property
    def Volume(self) -> float: ...
    @property
    def ConditionType(self) -> ConditionType: ...
    @ConditionType.setter
    def ConditionType(self, eConditionType: ConditionType) -> None: ...
    @property
    def SpaceType(self) -> SpaceType: ...
    @SpaceType.setter
    def SpaceType(self, eSpaceType: SpaceType) -> None: ...
    @property
    def SpaceTypeId(self) -> ElementId: ...
    @SpaceTypeId.setter
    def SpaceTypeId(self, spaceTypeId: ElementId) -> None: ...
    @property
    def SpaceConstruction(self) -> MEPSpaceConstruction: ...
    @property
    def CalculatedHeatingLoad(self) -> float: ...
    @property
    def DesignHeatingLoad(self) -> float: ...
    @DesignHeatingLoad.setter
    def DesignHeatingLoad(self, vDesignHeatingLoad: float) -> None: ...
    @property
    def CalculatedCoolingLoad(self) -> float: ...
    @property
    def DesignCoolingLoad(self) -> float: ...
    @DesignCoolingLoad.setter
    def DesignCoolingLoad(self, vDesignCoolingLoad: float) -> None: ...
    @property
    def OccupancyUnit(self) -> OccupancyUnit: ...
    @OccupancyUnit.setter
    def OccupancyUnit(self, eOccupancyUnit: OccupancyUnit) -> None: ...
    @property
    def BaseHeatLoadOn(self) -> BaseLoadOn: ...
    @BaseHeatLoadOn.setter
    def BaseHeatLoadOn(self, baseHeatLoadOn: BaseLoadOn) -> None: ...
    @property
    def NumberofPeople(self) -> float: ...
    @NumberofPeople.setter
    def NumberofPeople(self, vNumberofPeople: float) -> None: ...
    @property
    def AreaperPerson(self) -> float: ...
    @AreaperPerson.setter
    def AreaperPerson(self, vAreaperPerson: float) -> None: ...
    @property
    def SensibleHeatGainperPerson(self) -> float: ...
    @SensibleHeatGainperPerson.setter
    def SensibleHeatGainperPerson(self, vSensibleHeatGainperPerson: float) -> None: ...
    @property
    def LatentHeatGainperPerson(self) -> float: ...
    @LatentHeatGainperPerson.setter
    def LatentHeatGainperPerson(self, vLatentHeatGainperPerson: float) -> None: ...
    @property
    def LightingLoadUnit(self) -> BaseLoadOn: ...
    @LightingLoadUnit.setter
    def LightingLoadUnit(self, eLightingLoadUnit: BaseLoadOn) -> None: ...
    @property
    def ActualLightingLoad(self) -> float: ...
    @property
    def DesignLightingLoad(self) -> float: ...
    @DesignLightingLoad.setter
    def DesignLightingLoad(self, vDesignLightingLoad: float) -> None: ...
    @property
    def PowerLoadUnit(self) -> BaseLoadOn: ...
    @PowerLoadUnit.setter
    def PowerLoadUnit(self, ePowerLoadUnit: BaseLoadOn) -> None: ...
    @property
    def ActualPowerLoad(self) -> float: ...
    @property
    def DesignPowerLoad(self) -> float: ...
    @DesignPowerLoad.setter
    def DesignPowerLoad(self, vDesignPowerLoad: float) -> None: ...
    @property
    def Occupiable(self) -> bool: ...
    @property
    def Plenum(self) -> bool: ...
    def IsPointInSpace(self, point: XYZ) -> bool: ...


class SpaceTagType(FamilySymbol):


class FlexDuctType(MEPCurveType):


class Duct(MEPCurve):
    @property
    def DuctType(self) -> DuctType: ...
    @DuctType.setter
    def DuctType(self, ductType: DuctType) -> None: ...
    @property
    def IsPlaceholder(self) -> bool: ...
    @overload
    def Create(document: Document, ductTypeId: ElementId, levelId: ElementId, startConnector: Connector, endConnector: Connector) -> Duct: ...
    @overload
    def Create(document: Document, ductTypeId: ElementId, levelId: ElementId, startConnector: Connector, endPoint: XYZ) -> Duct: ...
    @overload
    def Create(document: Document, systemTypeId: ElementId, ductTypeId: ElementId, levelId: ElementId, startPoint: XYZ, endPoint: XYZ) -> Duct: ...
    def CreatePlaceholder(document: Document, systemTypeId: ElementId, ductTypeId: ElementId, levelId: ElementId, startPoint: XYZ, endPoint: XYZ) -> Duct: ...
    def SetSystemType(self, systemTypeId: ElementId) -> None: ...
    def IsHvacSystemTypeId(document: Document, systemTypeId: ElementId) -> bool: ...
    def IsDuctTypeId(document: Document, ductTypeId: ElementId) -> bool: ...


class DuctType(MEPCurveType):


class FlexDuct(MEPCurve):
    @property
    def Points(self) -> List[XYZ]: ...
    @Points.setter
    def Points(self, points: List[XYZ]) -> None: ...
    @property
    def FlexDuctType(self) -> FlexDuctType: ...
    @FlexDuctType.setter
    def FlexDuctType(self, flexDuctType: FlexDuctType) -> None: ...
    @property
    def StartTangent(self) -> XYZ: ...
    @StartTangent.setter
    def StartTangent(self, tangent: XYZ) -> None: ...
    @property
    def EndTangent(self) -> XYZ: ...
    @EndTangent.setter
    def EndTangent(self, tangent: XYZ) -> None: ...
    @overload
    def Create(document: Document, systemTypeId: ElementId, ductTypeId: ElementId, levelId: ElementId, startTangent: XYZ, endTangent: XYZ, points: List[XYZ]) -> FlexDuct: ...
    @overload
    def Create(document: Document, systemTypeId: ElementId, ductTypeId: ElementId, levelId: ElementId, points: List[XYZ]) -> FlexDuct: ...
    def IsFlexDuctTypeId(document: Document, ductTypeId: ElementId) -> bool: ...
    def IsHVACSystemTypeId(document: Document, systemTypeId: ElementId) -> bool: ...


class MechanicalSystem(MEPSystem):
    @property
    def SystemType(self) -> DuctSystemType: ...
    @property
    def BaseEquipmentConnector(self) -> Connector: ...
    @BaseEquipmentConnector.setter
    def BaseEquipmentConnector(self, baseEquipmentConnector: Connector) -> None: ...
    @property
    def DuctNetwork(self) -> ElementSet: ...
    @property
    def IsWellConnected(self) -> bool: ...
    def IsPressureDropServerMissing(self) -> bool: ...
    @overload
    def Create(ADocument: Document, typeId: ElementId, name: str) -> MechanicalSystem: ...
    @overload
    def Create(ADocument: Document, typeId: ElementId) -> MechanicalSystem: ...
    def GetFlow(self) -> float: ...
    def GetStaticPressure(self) -> float: ...


class SpaceTag(SpatialElementTag):
    @property
    def Space(self) -> Space: ...
    @property
    def SpaceTagType(self) -> SpaceTagType: ...
    @SpaceTagType.setter
    def SpaceTagType(self, A_0: SpaceTagType) -> None: ...


class Zone(Element):
    @Name.setter
    def Name(self, valueString: str) -> None: ...
    @property
    def Phase(self) -> Phase: ...
    @property
    def IsDefaultZone(self) -> bool: ...
    @IsDefaultZone.setter
    def IsDefaultZone(self, bDefaultZone: bool) -> None: ...
    @property
    def Area(self) -> float: ...
    @property
    def GrossArea(self) -> float: ...
    @property
    def Volume(self) -> float: ...
    @property
    def GrossVolume(self) -> float: ...
    @property
    def Perimeter(self) -> float: ...
    @property
    def Spaces(self) -> SpaceSet: ...
    @property
    def Boundary(self) -> CurveArray: ...
    @property
    def ServiceType(self) -> ServiceType: ...
    @ServiceType.setter
    def ServiceType(self, eSpaceService: ServiceType) -> None: ...
    @property
    def CalculatedSupplyAirflow(self) -> float: ...
    @property
    def CalculatedHeatingLoad(self) -> float: ...
    @property
    def CalculatedCoolingLoad(self) -> float: ...
    @property
    def HeatingSetPoint(self) -> float: ...
    @HeatingSetPoint.setter
    def HeatingSetPoint(self, vHeatingSetPoint: float) -> None: ...
    @property
    def CoolingSetPoint(self) -> float: ...
    @CoolingSetPoint.setter
    def CoolingSetPoint(self, vCoolingSetPoint: float) -> None: ...
    @property
    def HeatingAirTemperature(self) -> float: ...
    @HeatingAirTemperature.setter
    def HeatingAirTemperature(self, vHeatingAirTemperature: float) -> None: ...
    @property
    def CoolingAirTemperature(self) -> float: ...
    @CoolingAirTemperature.setter
    def CoolingAirTemperature(self, vCoolingAirTemperature: float) -> None: ...
    @property
    def HumidificationSetPoint(self) -> float: ...
    @HumidificationSetPoint.setter
    def HumidificationSetPoint(self, vHumidificationSetPoint: float) -> None: ...
    @property
    def DehumidificationSetPoint(self) -> float: ...
    @DehumidificationSetPoint.setter
    def DehumidificationSetPoint(self, vDehumidificationSetPoint: float) -> None: ...
    def AddSpaces(self, spaces: SpaceSet) -> bool: ...
    def RemoveSpaces(self, spaces: SpaceSet) -> bool: ...


class DuctSizeIterator:
    @property
    def IsValidObject(self) -> bool: ...
    def MoveNext(self) -> bool: ...
    def IsDone(self) -> bool: ...
    def Reset(self) -> None: ...
    def GetCurrent(self) -> MEPSize: ...
    def HasCurrent(self) -> bool: ...
    @property
    def Current(self) -> MEPSize: ...
    def Dispose(self) -> None: ...


class DuctSizes:
    def GetDuctSizeIterator(self) -> DuctSizeIterator: ...
    @property
    def Count(self) -> int: ...
    @property
    def IsValidObject(self) -> bool: ...
    def Contains(self, nominalDiameter: float) -> bool: ...
    def GetEnumerator(self) -> IEnumerator: ...
    def Dispose(self) -> None: ...


class DuctSizeSettingIterator:
    def Dispose(self) -> None: ...
    @property
    def IsValidObject(self) -> bool: ...
    def MoveNext(self) -> bool: ...
    def IsDone(self) -> bool: ...
    def Reset(self) -> None: ...
    def HasCurrent(self) -> bool: ...
    @property
    def Current(self) -> KeyValuePair: ...


class DuctSizeSettings(Element):
    def GetDuctSizeSettingIterator(self) -> DuctSizeSettingIterator: ...
    @property
    def Item(self, ductShape: DuctShape) -> DuctSizes: ...
    def GetSizeCount(self, shape: DuctShape) -> int: ...
    def GetDuctSizeSettings(aDoc: Document) -> DuctSizeSettings: ...
    def AddSize(self, shape: DuctShape, sizeInfo: MEPSize) -> None: ...
    def RemoveSize(self, shape: DuctShape, nominalDiameter: float) -> None: ...
    def GetEnumerator(self) -> IEnumerator: ...


class DuctShape:
    Round = 0
    Rectangular = 1
    Oval = 2


class MechanicalEquipment(MEPModel):


class MechanicalFitting(MEPModel):
    @property
    def PartType(self) -> PartType: ...


class ComponentClassification:
    Undefined = 0
    Pipe = 1
    Duct = 2
    FlexPipe = 11
    FlexDuct = 12
    Elbow = 101
    Tee = 102
    Tap = 103
    Transition = 104
    Cross = 105
    Endcap = 106
    Coupling = 107
    Union = 108
    Flange = 109
    Wye = 110
    Valve = 111
    Sensor = 112
    Hanger = 113
    Sleeve = 114


class MEPBuildingConstruction(ElementType):
    def GetConstructions(self, constructionType: ConstructionType) -> ICollection: ...
    def GetBuildingConstruction(self, constructionType: ConstructionType) -> Construction: ...
    def SetBuildingConstruction(self, constructionType: ConstructionType, buildingConstruction: Construction) -> None: ...
    def SetBuildingConstructionOverride(self, constructionType: ConstructionType, override: bool) -> None: ...
    def GetBuildingConstructionOverride(self, constructionType: ConstructionType) -> bool: ...


class MEPBuildingConstructionSet(APIObject):
    def __init__(self): ...
    def Clear(self) -> None: ...
    @property
    def Size(self) -> int: ...
    @property
    def IsEmpty(self) -> bool: ...
    def ForwardIterator(self) -> MEPBuildingConstructionSetIterator: ...
    def ReverseIterator(self) -> MEPBuildingConstructionSetIterator: ...
    def GetEnumerator(self) -> IEnumerator: ...
    def Contains(self, item: MEPBuildingConstruction) -> bool: ...
    def Insert(self, item: MEPBuildingConstruction) -> bool: ...
    def Erase(self, item: MEPBuildingConstruction) -> int: ...


class MEPBuildingConstructionSetIterator(APIObject):
    def __init__(self): ...
    @property
    def Current(self) -> Object: ...
    def MoveNext(self) -> bool: ...
    def Reset(self) -> None: ...


class MEPSpaceConstruction:
    @property
    def CurrentConstruction(self) -> MEPBuildingConstruction: ...
    @CurrentConstruction.setter
    def CurrentConstruction(self, pCurrentConstruction: MEPBuildingConstruction) -> None: ...
    @property
    def SpaceConstructions(self) -> MEPBuildingConstructionSet: ...
    def NewConstruction(self, pName: str) -> MEPBuildingConstruction: ...
    def DuplicateConstruction(self, pCurrentConstruction: MEPBuildingConstruction, pName: str) -> MEPBuildingConstruction: ...
    def DeleteConstruction(self, pCurrentConstruction: MEPBuildingConstruction) -> None: ...


class DuctFittingAndAccessoryConnectorData:
    @property
    def Width(self) -> float: ...
    @property
    def Height(self) -> float: ...
    @property
    def Diameter(self) -> float: ...
    @property
    def Angle(self) -> float: ...
    @property
    def Index(self) -> int: ...
    @property
    def LinkIndex(self) -> int: ...
    @property
    def FlowDirection(self) -> FlowDirectionType: ...
    @property
    def Flow(self) -> float: ...
    @property
    def VelocityPressure(self) -> float: ...
    @property
    def Profile(self) -> ConnectorProfileType: ...
    @property
    def IsValidObject(self) -> bool: ...
    def GetCoordination(self) -> Transform: ...
    def Dispose(self) -> None: ...


class DuctFittingAndAccessoryData:
    @property
    def ServerGUID(self) -> Guid: ...
    @property
    def PartType(self) -> PartType: ...
    @property
    def SystemClassification(self) -> MEPSystemClassification: ...
    @property
    def Origin(self) -> XYZ: ...
    @property
    def AirViscosity(self) -> float: ...
    @property
    def IsValidObject(self) -> bool: ...
    def GetEntity(self) -> Entity: ...
    def GetAllConnectorData(self) -> List[DuctFittingAndAccessoryConnectorData]: ...
    def GetFamilyInstanceId(self) -> ElementId: ...
    def Dispose(self) -> None: ...


class DuctFittingAndAccessoryPressureDropItem:
    @property
    def BeginConnectorIndex(self) -> int: ...
    @property
    def EndConnectorIndex(self) -> int: ...
    @property
    def VelocityPressure(self) -> float: ...
    @property
    def Coefficient(self) -> float: ...
    @Coefficient.setter
    def Coefficient(self, coefficient: float) -> None: ...
    @property
    def IsValidObject(self) -> bool: ...
    def Dispose(self) -> None: ...


class DuctFittingAndAccessoryPressureDropData:
    @property
    def CalculationType(self) -> int: ...
    @property
    def IsCurrentEntityValid(self) -> bool: ...
    @IsCurrentEntityValid.setter
    def IsCurrentEntityValid(self, isCurrentEntityValid: bool) -> None: ...
    @property
    def IsValidObject(self) -> bool: ...
    def GetDuctFittingAndAccessoryData(self) -> DuctFittingAndAccessoryData: ...
    def GetPresureDropItems(self) -> List[DuctFittingAndAccessoryPressureDropItem]: ...
    def SetDefaultEntity(self, defaultEntity: Entity) -> None: ...
    def Dispose(self) -> None: ...


class DuctPressureDropData:
    @property
    def Level(self) -> SystemCalculationLevel: ...
    @property
    def Shape(self) -> ConnectorProfileType: ...
    @property
    def CategoryId(self) -> ElementId: ...
    @property
    def Height(self) -> float: ...
    @property
    def WidthOrDiameter(self) -> float: ...
    @property
    def Length(self) -> float: ...
    @property
    def Density(self) -> float: ...
    @property
    def Viscosity(self) -> float: ...
    @property
    def Roughness(self) -> float: ...
    @property
    def Flow(self) -> float: ...
    @property
    def EquivalentDiameter(self) -> float: ...
    @EquivalentDiameter.setter
    def EquivalentDiameter(self, equivalentDiameter: float) -> None: ...
    @property
    def HydraulicDiameter(self) -> float: ...
    @HydraulicDiameter.setter
    def HydraulicDiameter(self, hydraulicDiameter: float) -> None: ...
    @property
    def ReynoldsNumber(self) -> float: ...
    @ReynoldsNumber.setter
    def ReynoldsNumber(self, reynoldsNumber: float) -> None: ...
    @property
    def Velocity(self) -> float: ...
    @Velocity.setter
    def Velocity(self, velocity: float) -> None: ...
    @property
    def VelocityPressure(self) -> float: ...
    @VelocityPressure.setter
    def VelocityPressure(self, velocityPressure: float) -> None: ...
    @property
    def Friction(self) -> float: ...
    @Friction.setter
    def Friction(self, friction: float) -> None: ...
    @property
    def PressureDrop(self) -> float: ...
    @PressureDrop.setter
    def PressureDrop(self, pressureDrop: float) -> None: ...
    @property
    def Coefficient(self) -> float: ...
    @Coefficient.setter
    def Coefficient(self, coefficient: float) -> None: ...
    @property
    def IsValidObject(self) -> bool: ...
    def Dispose(self) -> None: ...


class IDuctFittingAndAccessoryPressureDropServer:
    def Calculate(self, data: DuctFittingAndAccessoryPressureDropData) -> bool: ...
    def IsApplicable(self, data: DuctFittingAndAccessoryPressureDropData) -> bool: ...
    def GetDataSchema(self) -> Schema: ...


class IDuctPressureDropServer:
    def Calculate(self, data: DuctPressureDropData) -> None: ...
    def GetInformationLink(self) -> str: ...
    def GetHtmlDescription(self) -> str: ...


class MechanicalEquipmentSet(Element):
    @property
    def Classification(self) -> EquipmentClassification: ...
    @property
    def OnDuty(self) -> int: ...
    @OnDuty.setter
    def OnDuty(self, number: int) -> None: ...
    @property
    def OnStandby(self) -> int: ...
    @OnStandby.setter
    def OnStandby(self, number: int) -> None: ...
    def Create(document: Document, typeId: ElementId, memberIds: ISet) -> MechanicalEquipmentSet: ...
    def AreElementsNotConnectedInSeries(document: Document, elemIds: ISet) -> bool: ...
    def AreValidMembers(document: Document, memberIds: ISet) -> bool: ...
    def GetMembers(self) -> ISet: ...
    def Add(self, elemIds: ISet) -> None: ...
    def Remove(self, elemIds: ISet) -> None: ...


class MechanicalEquipmentSetType(ElementType):
    def Create(document: Document, name: str) -> MechanicalEquipmentSetType: ...


class MechanicalUtils:
    def ConvertDuctPlaceholders(document: Document, placeholderIds: ICollection) -> ICollection: ...
    @overload
    def ConnectDuctPlaceholdersAtElbow(document: Document, connector1: Connector, connector2: Connector) -> bool: ...
    @overload
    def ConnectDuctPlaceholdersAtElbow(document: Document, placeholder1Id: ElementId, placeholder2Id: ElementId) -> bool: ...
    @overload
    def ConnectDuctPlaceholdersAtTee(document: Document, connector1: Connector, connector2: Connector, connector3: Connector) -> bool: ...
    @overload
    def ConnectDuctPlaceholdersAtTee(document: Document, placeholder1Id: ElementId, placeholder2Id: ElementId) -> bool: ...
    @overload
    def ConnectDuctPlaceholdersAtCross(document: Document, connector1: Connector, connector2: Connector, connector3: Connector, connector4: Connector) -> bool: ...
    @overload
    def ConnectDuctPlaceholdersAtCross(document: Document, placeholder1Id: ElementId, placeholder2Id: ElementId, placeholder3Id: ElementId) -> bool: ...
    @overload
    def ConnectDuctPlaceholdersAtCross(document: Document, placeholder1Id: ElementId, placeholder2Id: ElementId) -> bool: ...
    def ConnectAirTerminalOnDuct(document: Document, airTerminalId: ElementId, ductCurveId: ElementId) -> bool: ...
    def BreakCurve(document: Document, ductId: ElementId, ptBreak: XYZ) -> ElementId: ...


class DuctInsulation(InsulationLiningBase):
    def Create(document: Document, ductOrContentElementId: ElementId, ductInsulationTypeId: ElementId, Thickness: float) -> DuctInsulation: ...


class DuctInsulationType(ElementType):


class DuctLining(InsulationLiningBase):
    def Create(document: Document, ductOrContentElementId: ElementId, ductLiningTypeId: ElementId, Thickness: float) -> DuctLining: ...


class DuctLiningType(ElementType):
    @property
    def Roughness(self) -> float: ...
    @Roughness.setter
    def Roughness(self, roughness: float) -> None: ...
    def IsValidRoughness(self, roughness: float) -> bool: ...


class DuctSettings(Element):
    @property
    def RectangularDuctSizeSeparator(self) -> str: ...
    @RectangularDuctSizeSeparator.setter
    def RectangularDuctSizeSeparator(self, rectangularDuctSizeSeparator: str) -> None: ...
    @property
    def RectangularDuctSizeSuffix(self) -> str: ...
    @RectangularDuctSizeSuffix.setter
    def RectangularDuctSizeSuffix(self, rectangularDuctSizeSuffix: str) -> None: ...
    @property
    def RoundDuctSizeSuffix(self) -> str: ...
    @RoundDuctSizeSuffix.setter
    def RoundDuctSizeSuffix(self, roundDuctSizeSuffix: str) -> None: ...
    @property
    def RoundDuctSizePrefix(self) -> str: ...
    @RoundDuctSizePrefix.setter
    def RoundDuctSizePrefix(self, roundDuctSizePrefix: str) -> None: ...
    @property
    def ConnectorSeparator(self) -> str: ...
    @ConnectorSeparator.setter
    def ConnectorSeparator(self, connectorSeparator: str) -> None: ...
    @property
    def OvalDuctSizeSeparator(self) -> str: ...
    @OvalDuctSizeSeparator.setter
    def OvalDuctSizeSeparator(self, ovalDuctSizeSeparator: str) -> None: ...
    @property
    def OvalDuctSizeSuffix(self) -> str: ...
    @OvalDuctSizeSuffix.setter
    def OvalDuctSizeSuffix(self, ovalDuctSizeSuffix: str) -> None: ...
    @property
    def FlatOnTop(self) -> str: ...
    @FlatOnTop.setter
    def FlatOnTop(self, flatOnTop: str) -> None: ...
    @property
    def FlatOnBottom(self) -> str: ...
    @FlatOnBottom.setter
    def FlatOnBottom(self, flatOnBottom: str) -> None: ...
    @property
    def SetUp(self) -> str: ...
    @SetUp.setter
    def SetUp(self, setUp: str) -> None: ...
    @property
    def SetDown(self) -> str: ...
    @SetDown.setter
    def SetDown(self, setDown: str) -> None: ...
    @property
    def SetUpFromBottom(self) -> str: ...
    @SetUpFromBottom.setter
    def SetUpFromBottom(self, setUpFromBottom: str) -> None: ...
    @property
    def SetDownFromBottom(self) -> str: ...
    @SetDownFromBottom.setter
    def SetDownFromBottom(self, setDownFromBottom: str) -> None: ...
    @property
    def Centerline(self) -> str: ...
    @Centerline.setter
    def Centerline(self, centerline: str) -> None: ...
    @property
    def AirDensity(self) -> float: ...
    @AirDensity.setter
    def AirDensity(self, airDensity: float) -> None: ...
    @property
    def AirViscosity(self) -> float: ...
    @AirViscosity.setter
    def AirViscosity(self, airViscosity: float) -> None: ...
    @property
    def FittingAnnotationSize(self) -> float: ...
    @FittingAnnotationSize.setter
    def FittingAnnotationSize(self, fittingAnnotationSize: float) -> None: ...
    @property
    def RiseDropAnnotationSize(self) -> float: ...
    @RiseDropAnnotationSize.setter
    def RiseDropAnnotationSize(self, riseDropAnnotationSize: float) -> None: ...
    @property
    def FittingAngleUsage(self) -> FittingAngleUsage: ...
    @FittingAngleUsage.setter
    def FittingAngleUsage(self, fittingAngleUsage: FittingAngleUsage) -> None: ...
    @property
    def UseAnnotationScaleForSingleLineFittings(self) -> bool: ...
    @UseAnnotationScaleForSingleLineFittings.setter
    def UseAnnotationScaleForSingleLineFittings(self, useAnnotationScaleForSingleLineFittings: bool) -> None: ...
    def GetDuctSettings(document: Document) -> DuctSettings: ...
    def GetSpecificFittingAngles(self) -> List[float]: ...
    def SetSpecificFittingAngleStatus(self, angle: float, useInLayout: bool) -> None: ...
    def GetSpecificFittingAngleStatus(self, angle: float) -> bool: ...
    def IsValidSpecificFittingAngle(self, angle: float) -> bool: ...
    def GetPressLossCalculationServerInfo(self) -> MEPCalculationServerInfo: ...
    def SetPressLossCalculationServerInfo(self, serverInfo: MEPCalculationServerInfo) -> None: ...


class MechanicalSystemType(MEPSystemType):
    @property
    def RiseDropSettings(self) -> RiseDropSymbol: ...
    @RiseDropSettings.setter
    def RiseDropSettings(self, RiseDropSettings: RiseDropSymbol) -> None: ...
    def Create(ADoc: Document, systemClassification: MEPSystemClassification, name: str) -> MechanicalSystemType: ...
    def ValidateRiseDropSymbolType(self, risedropType: RiseDropSymbol) -> bool: ...


class MEPSection:
    @property
    def Number(self) -> int: ...
    @property
    def Roughness(self) -> float: ...
    @property
    def Flow(self) -> float: ...
    @property
    def FixtureUnit(self) -> float: ...
    @property
    def Friction(self) -> float: ...
    @property
    def Velocity(self) -> float: ...
    @property
    def VelocityPressure(self) -> float: ...
    @property
    def TotalCoefficient(self) -> float: ...
    @property
    def TotalPressureLoss(self) -> float: ...
    @property
    def TotalCurveLength(self) -> float: ...
    @property
    def ReynoldsNumber(self) -> float: ...
    @property
    def FrictionFactor(self) -> float: ...
    @property
    def IsValidObject(self) -> bool: ...
    def GetPressureDrop(self, elemId: ElementId) -> float: ...
    def GetCoefficient(self, elemId: ElementId) -> float: ...
    def GetSegmentLength(self, segmentId: ElementId) -> float: ...
    def IsMain(self, fittingId: ElementId) -> bool: ...
    def GetElementIds(self) -> List[ElementId]: ...
    def Dispose(self) -> None: ...


class SpaceFilter(ElementSlowFilter):
    def __init__(self): ...


class SpaceTagFilter(ElementSlowFilter):
    def __init__(self): ...
