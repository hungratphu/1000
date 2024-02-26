from typing import Tuple, Set, Iterable, List


class DirectContext3DHandleSettings:
    @overload
    def __init__(self, other: DirectContext3DHandleSettings): ...
    @overload
    def __init__(self, visibility: bool, transparency: int): ...
    @overload
    def __init__(self): ...
    @property
    def Visibility(self) -> bool: ...
    @Visibility.setter
    def Visibility(self, visibility: bool) -> None: ...
    @property
    def IsValidObject(self) -> bool: ...
    def Assign(self, other: DirectContext3DHandleSettings) -> None: ...
    def IsEqual(self, other: DirectContext3DHandleSettings) -> bool: ...
    def SetTransparency(self, transparency: int) -> None: ...
    def GetTransparency(self) -> int: ...
    def Dispose(self) -> None: ...


class DirectContext3DHandleOverrides:
    @property
    def IsValidObject(self) -> bool: ...
    def IsEqual(self, other: DirectContext3DHandleOverrides) -> bool: ...
    def Assign(self, other: DirectContext3DHandleOverrides) -> None: ...
    def GetDirectContext3DHandleSettings(self, aDoc: Document, elementId: ElementId) -> DirectContext3DHandleSettings: ...
    def SetDirectContext3DHandleSettings(self, aDoc: Document, elementId: ElementId, newSettings: DirectContext3DHandleSettings) -> None: ...
    def Dispose(self) -> None: ...


class IDirectContext3DServer:
    def CanExecute(self, dBView: View) -> bool: ...
    def GetApplicationId(self) -> str: ...
    def GetSourceId(self) -> str: ...
    def UsesHandles(self) -> bool: ...
    def GetBoundingBox(self, dBView: View) -> Outline: ...
    def UseInTransparentPass(self, dBView: View) -> bool: ...
    def RenderScene(self, dBView: View, displayStyle: DisplayStyle) -> None: ...


class Vertex:
    @property
    def IsValidObject(self) -> bool: ...
    def Dispose(self) -> None: ...


class VertexPosition(Vertex):
    def __init__(self, position: XYZ): ...
    @property
    def Position(self) -> XYZ: ...
    @Position.setter
    def Position(self, position: XYZ) -> None: ...
    def GetSizeInFloats() -> int: ...


class VertexPositionNormal(Vertex):
    def __init__(self, position: XYZ, normal: XYZ): ...
    @property
    def Position(self) -> XYZ: ...
    @Position.setter
    def Position(self, position: XYZ) -> None: ...
    @property
    def Normal(self) -> XYZ: ...
    @Normal.setter
    def Normal(self, normal: XYZ) -> None: ...
    def GetSizeInFloats() -> int: ...


class VertexPositionColored(Vertex):
    def __init__(self, position: XYZ, color: ColorWithTransparency): ...
    @property
    def Position(self) -> XYZ: ...
    @Position.setter
    def Position(self, position: XYZ) -> None: ...
    def GetColor(self) -> ColorWithTransparency: ...
    def SetColor(self, color: ColorWithTransparency) -> None: ...
    def GetSizeInFloats() -> int: ...


class VertexPositionNormalColored(Vertex):
    def __init__(self, position: XYZ, normal: XYZ, color: ColorWithTransparency): ...
    @property
    def Position(self) -> XYZ: ...
    @Position.setter
    def Position(self, position: XYZ) -> None: ...
    @property
    def Normal(self) -> XYZ: ...
    @Normal.setter
    def Normal(self, normal: XYZ) -> None: ...
    def GetColor(self) -> ColorWithTransparency: ...
    def SetColor(self, color: ColorWithTransparency) -> None: ...
    def GetSizeInFloats() -> int: ...


class VertexStream:
    @property
    def IsValidObject(self) -> bool: ...
    def Dispose(self) -> None: ...


class VertexStreamPosition(VertexStream):
    def AddVertex(self, vertex: VertexPosition) -> None: ...
    def AddVertices(self, vertices: List[VertexPosition]) -> None: ...


class VertexStreamPositionNormal(VertexStream):
    def AddVertex(self, vertex: VertexPositionNormal) -> None: ...
    def AddVertices(self, vertices: List[VertexPositionNormal]) -> None: ...


class VertexStreamPositionColored(VertexStream):
    def AddVertex(self, vertex: VertexPositionColored) -> None: ...
    def AddVertices(self, vertices: List[VertexPositionColored]) -> None: ...


class VertexStreamPositionNormalColored(VertexStream):
    def AddVertex(self, vertex: VertexPositionNormalColored) -> None: ...
    def AddVertices(self, vertices: List[VertexPositionNormalColored]) -> None: ...


class VertexBuffer:
    def __init__(self, sizeInFloats: int): ...
    @property
    def IsValidObject(self) -> bool: ...
    def IsValid(self) -> bool: ...
    def Map(self, sizeInFloats: int) -> None: ...
    def Unmap(self) -> None: ...
    def GetVertexStreamPosition(self) -> VertexStreamPosition: ...
    def GetVertexStreamPositionNormal(self) -> VertexStreamPositionNormal: ...
    def GetVertexStreamPositionColored(self) -> VertexStreamPositionColored: ...
    def GetVertexStreamPositionNormalColored(self) -> VertexStreamPositionNormalColored: ...
    def GetMappedHandle(self) -> IntPtr: ...
    def Dispose(self) -> None: ...


class IndexPrimitive:
    @property
    def IsValidObject(self) -> bool: ...
    def Dispose(self) -> None: ...


class IndexPoint(IndexPrimitive):
    def __init__(self, index: int): ...
    @property
    def Index(self) -> int: ...
    @Index.setter
    def Index(self, index: int) -> None: ...
    def GetSizeInShortInts() -> int: ...


class IndexLine(IndexPrimitive):
    def __init__(self, index0: int, index1: int): ...
    @property
    def Index0(self) -> int: ...
    @Index0.setter
    def Index0(self, index0: int) -> None: ...
    @property
    def Index1(self) -> int: ...
    @Index1.setter
    def Index1(self, index1: int) -> None: ...
    def GetSizeInShortInts() -> int: ...


class IndexTriangle(IndexPrimitive):
    def __init__(self, index0: int, index1: int, index2: int): ...
    @property
    def Index0(self) -> int: ...
    @Index0.setter
    def Index0(self, index0: int) -> None: ...
    @property
    def Index1(self) -> int: ...
    @Index1.setter
    def Index1(self, index1: int) -> None: ...
    @property
    def Index2(self) -> int: ...
    @Index2.setter
    def Index2(self, index2: int) -> None: ...
    def GetSizeInShortInts() -> int: ...


class IndexStream:
    @property
    def IsValidObject(self) -> bool: ...
    def Dispose(self) -> None: ...


class IndexStreamPoint(IndexStream):
    def AddPoint(self, point: IndexPoint) -> None: ...
    def AddPoints(self, points: List[IndexPoint]) -> None: ...


class IndexStreamLine(IndexStream):
    def AddLine(self, line: IndexLine) -> None: ...
    def AddLines(self, lines: List[IndexLine]) -> None: ...


class IndexStreamTriangle(IndexStream):
    def AddTriangle(self, triangle: IndexTriangle) -> None: ...
    def AddTriangles(self, triangles: List[IndexTriangle]) -> None: ...


class IndexBuffer:
    def __init__(self, sizeInShortInts: int): ...
    @property
    def IsValidObject(self) -> bool: ...
    def IsValid(self) -> bool: ...
    def Map(self, sizeInShortInts: int) -> None: ...
    def Unmap(self) -> None: ...
    def GetIndexStreamPoint(self) -> IndexStreamPoint: ...
    def GetIndexStreamLine(self) -> IndexStreamLine: ...
    def GetIndexStreamTriangle(self) -> IndexStreamTriangle: ...
    def GetMappedHandle(self) -> IntPtr: ...
    def Dispose(self) -> None: ...


class EffectInstance:
    def __init__(self, vertexFormatBits: VertexFormatBits): ...
    @property
    def IsValidObject(self) -> bool: ...
    def IsValid(self) -> bool: ...
    def MatchesFormat(self, vertexFormat: VertexFormat) -> bool: ...
    def SetColor(self, color: Color) -> None: ...
    def SetAmbientColor(self, color: Color) -> None: ...
    def SetDiffuseColor(self, color: Color) -> None: ...
    def SetEmissiveColor(self, color: Color) -> None: ...
    def SetSpecularColor(self, color: Color) -> None: ...
    def SetGlossiness(self, glossiness: float) -> None: ...
    def SetTransparency(self, transparency: float) -> None: ...
    def Dispose(self) -> None: ...


class VertexFormat:
    def __init__(self, vertexFormatBits: VertexFormatBits): ...
    @property
    def IsValidObject(self) -> bool: ...
    def IsValid(self) -> bool: ...
    def Dispose(self) -> None: ...


class ClipPlane:
    def __init__(self, other: ClipPlane): ...
    @property
    def Origin(self) -> XYZ: ...
    @Origin.setter
    def Origin(self, origin: XYZ) -> None: ...
    @property
    def Normal(self) -> XYZ: ...
    @Normal.setter
    def Normal(self, normal: XYZ) -> None: ...
    @property
    def IsValidObject(self) -> bool: ...
    def Dispose(self) -> None: ...


class DrawContext:
    def FlushBuffer(vertexBuffer: VertexBuffer, vertexCount: int, indexBuffer: IndexBuffer, indexCount: int, vertexFormat: VertexFormat, effectInstance: EffectInstance, primitiveType: PrimitiveType, start: int, primitiveCount: int) -> None: ...
    def IsInterrupted() -> bool: ...
    def GetViewRectangle() -> Rectangle: ...
    def GetClipRectangle() -> Rectangle: ...
    def GetClipPlanes() -> List[ClipPlane]: ...
    def GetCamera() -> Camera: ...
    def IsTransparentPass() -> bool: ...
    def GetOverrideColor() -> Tuple[bool, Color]: ...
    def GetOverrideTransparency() -> Tuple[bool, float]: ...
    def SetWorldTransform(trf: Transform) -> None: ...
    def IsAvailable() -> bool: ...


class Camera:
    def __init__(self, other: Camera): ...
    @property
    def EyePosition(self) -> XYZ: ...
    @EyePosition.setter
    def EyePosition(self, eyePosition: XYZ) -> None: ...
    @property
    def ViewDirection(self) -> XYZ: ...
    @ViewDirection.setter
    def ViewDirection(self, viewDirection: XYZ) -> None: ...
    @property
    def UpDirection(self) -> XYZ: ...
    @UpDirection.setter
    def UpDirection(self, upDirection: XYZ) -> None: ...
    @property
    def ProjectionMethod(self) -> ProjectionMethod: ...
    @ProjectionMethod.setter
    def ProjectionMethod(self, projectionMethod: ProjectionMethod) -> None: ...
    @property
    def TargetDistance(self) -> float: ...
    @TargetDistance.setter
    def TargetDistance(self, targetDistance: float) -> None: ...
    @property
    def HorizontalExtent(self) -> float: ...
    @HorizontalExtent.setter
    def HorizontalExtent(self, horizontalExtent: float) -> None: ...
    @property
    def HorizontalOffset(self) -> float: ...
    @HorizontalOffset.setter
    def HorizontalOffset(self, horizontalOffset: float) -> None: ...
    @property
    def VerticalExtent(self) -> float: ...
    @VerticalExtent.setter
    def VerticalExtent(self, verticalExtent: float) -> None: ...
    @property
    def VerticalOffset(self) -> float: ...
    @VerticalOffset.setter
    def VerticalOffset(self, verticalOffset: float) -> None: ...
    @property
    def NearDistance(self) -> float: ...
    @NearDistance.setter
    def NearDistance(self, nearDistance: float) -> None: ...
    @property
    def FarDistance(self) -> float: ...
    @FarDistance.setter
    def FarDistance(self, farDistance: float) -> None: ...
    @property
    def IsValidObject(self) -> bool: ...
    def Transform(self, trf: Transform) -> None: ...
    def Dispose(self) -> None: ...


class DirectContext3DDocumentUtils:
    def IsADirectContext3DHandleCategory(categoryId: ElementId) -> bool: ...
    def IsADirectContext3DHandleType(aDocument: Document, elementId: ElementId) -> bool: ...
    def IsADirectContext3DHandleInstance(aDocument: Document, elementId: ElementId) -> bool: ...
    def GetDirectContext3DHandleTypes(aDocument: Document, handleCategory: ElementId) -> ISet: ...
    def GetDirectContext3DHandleInstances(aDocument: Document, handleCategory: ElementId) -> ISet: ...


class VertexFormatBits:
    Position = 1
    PositionNormal = 3
    PositionColored = 5
    PositionNormalColored = 7


class PrimitiveType:
    TriangleList = 0
    LineList = 1
    PointList = 2


class ProjectionMethod:
    Orthographic = 0
    Perspective = 1
