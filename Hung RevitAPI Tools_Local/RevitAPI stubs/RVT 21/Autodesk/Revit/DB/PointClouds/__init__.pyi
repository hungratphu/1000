from typing import Tuple, Set, Iterable, List


class CloudPoint:
    def __init__(self, x: Single, y: Single, z: Single, color: int): ...
    def op_Implicit(cp: CloudPoint) -> XYZ: ...


class PointIterator:
    @property
    def Current(self) -> CloudPoint: ...
    @property
    def CurrentObject(self) -> Object: ...
    @property
    def IsValidObject(self) -> bool: ...
    def MoveNext(self) -> bool: ...
    def IsDone(self) -> bool: ...
    def Reset(self) -> None: ...
    def Free(self) -> None: ...
    def Dispose(self) -> None: ...


class PointCollection:
    def GetPointIterator(self) -> PointIterator: ...
    @property
    def Count(self) -> int: ...
    @property
    def IsValidObject(self) -> bool: ...
    def GetPointBufferPointer(self) -> IntPtr: ...
    def GetEnumerator(self) -> IEnumerator: ...
    def Dispose(self) -> None: ...


class IPointSetIterator:
    def Free(self) -> None: ...
    def ReadPoints(self, buffer: IntPtr, bufferSize: int) -> int: ...


class IPointCloudAccess:
    def GetUnitsToFeetConversionFactor(self) -> float: ...
    @overload
    def CreatePointSetIterator(self, rFilter: PointCloudFilter, density: float, viewId: ElementId) -> IPointSetIterator: ...
    @overload
    def CreatePointSetIterator(self, rFilter: PointCloudFilter, viewId: ElementId) -> IPointSetIterator: ...
    def ReadPoints(self, rFilter: PointCloudFilter, viewId: ElementId, buffer: IntPtr, nBufferSize: int) -> int: ...
    def GetOffset(self) -> XYZ: ...
    def GetExtent(self) -> Outline: ...
    def GetName(self) -> str: ...
    def GetColorEncoding(self) -> PointCloudColorEncoding: ...
    def Free(self) -> None: ...


class IPointCloudEngine:
    def CreatePointCloudAccess(self, identifier: str) -> IPointCloudAccess: ...
    def Free(self) -> None: ...


class PointCloudEngineRegistry:
    def RegisterPointCloudEngine(identifier: str, engine: IPointCloudEngine, isFileBased: bool) -> None: ...
    def GetSupportedEngines() -> List[str]: ...
    def IsEngineFileBased(identifier: str) -> bool: ...
    def UnregisterPointCloudEngine(identifier: str) -> None: ...


class PointCloudFilter:
    def TestPoint(self, point: CloudPoint) -> bool: ...
    @property
    def IsValidObject(self) -> bool: ...
    def TestCell(self, min: XYZ, max: XYZ) -> int: ...
    def PrepareForCell(self, min: XYZ, max: XYZ, numTests: int) -> None: ...
    def Clone(self) -> PointCloudFilter: ...
    def Dispose(self) -> None: ...


class PointCloudColorEncoding:
    ARGB = 0
    ABGR = 1


class PointCloudColorSettings:
    @overload
    def __init__(self, other: PointCloudColorSettings): ...
    @overload
    def __init__(self, color1: Color, color2: Color): ...
    @overload
    def __init__(self, mode: PointCloudColorMode): ...
    @overload
    def __init__(self): ...
    @property
    def Color1(self) -> Color: ...
    @property
    def Color2(self) -> Color: ...
    @property
    def IsValidObject(self) -> bool: ...
    def Assign(self, other: PointCloudColorSettings) -> None: ...
    def IsEqual(self, other: PointCloudColorSettings) -> bool: ...
    def Dispose(self) -> None: ...


class PointCloudOverrideSettings:
    @overload
    def __init__(self, other: PointCloudOverrideSettings): ...
    @overload
    def __init__(self): ...
    @property
    def Visible(self) -> bool: ...
    @Visible.setter
    def Visible(self, visible: bool) -> None: ...
    @property
    def ColorMode(self) -> PointCloudColorMode: ...
    @ColorMode.setter
    def ColorMode(self, colorMode: PointCloudColorMode) -> None: ...
    @property
    def IsValidObject(self) -> bool: ...
    def Assign(self, other: PointCloudOverrideSettings) -> None: ...
    def IsEqual(self, other: PointCloudOverrideSettings) -> bool: ...
    def SetModeOverride(self, mode: PointCloudColorMode, colorSettings: PointCloudColorSettings) -> None: ...
    def GetModeOverride(self, mode: PointCloudColorMode) -> PointCloudColorSettings: ...
    def Dispose(self) -> None: ...


class PointCloudOverrides:
    def __init__(self): ...
    @property
    def IsValidObject(self) -> bool: ...
    def IsEqual(self, other: PointCloudOverrides) -> bool: ...
    def Assign(self, other: PointCloudOverrides) -> None: ...
    @overload
    def GetPointCloudScanOverrideSettings(self, elementId: ElementId, scanTag: str, doc: Document) -> PointCloudOverrideSettings: ...
    @overload
    def GetPointCloudScanOverrideSettings(self, elementId: ElementId) -> PointCloudOverrideSettings: ...
    @overload
    def GetPointCloudRegionOverrideSettings(self, elementId: ElementId, regionTag: str, doc: Document) -> PointCloudOverrideSettings: ...
    @overload
    def GetPointCloudRegionOverrideSettings(self, elementId: ElementId) -> PointCloudOverrideSettings: ...
    @overload
    def SetPointCloudScanOverrideSettings(self, elementId: ElementId, newSettings: PointCloudOverrideSettings, scanTag: str, doc: Document) -> None: ...
    @overload
    def SetPointCloudScanOverrideSettings(self, elementId: ElementId, newSettings: PointCloudOverrideSettings) -> None: ...
    @overload
    def SetPointCloudRegionOverrideSettings(self, elementId: ElementId, newSettings: PointCloudOverrideSettings, regionTag: str, doc: Document) -> None: ...
    @overload
    def SetPointCloudRegionOverrideSettings(self, elementId: ElementId, newSettings: PointCloudOverrideSettings) -> None: ...
    def ArePointCloudOverrideSettingsValid(tag: str, settings: PointCloudOverrideSettings) -> bool: ...
    def Dispose(self) -> None: ...


class PointCloudFilterFactory:
    @overload
    def CreateMultiPlaneFilter(planes: List[Plane]) -> PointCloudFilter: ...
    @overload
    def CreateMultiPlaneFilter(planes: List[Plane], exactPlaneCount: int) -> PointCloudFilter: ...


class PointCloudFilterUtils:
    def GetFilteredOutline(filter: PointCloudFilter, box: Outline) -> Outline: ...
