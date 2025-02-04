#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
# Using build pattern: cmake
# autospec version: v21
# autospec commit: 94c6be0
#
Name     : qt6scxml
Version  : 6.8.2
Release  : 23
URL      : https://download.qt.io/official_releases/qt/6.8/6.8.2/submodules/qtscxml-everywhere-src-6.8.2.zip
Source0  : https://download.qt.io/official_releases/qt/6.8/6.8.2/submodules/qtscxml-everywhere-src-6.8.2.zip
Summary  : No detailed summary available
Group    : Development/Tools
License  : Apache-2.0 BSD-3-Clause GPL-2.0 GPL-3.0 LGPL-3.0
Requires: qt6scxml-lib = %{version}-%{release}
Requires: qt6scxml-libexec = %{version}-%{release}
Requires: qt6scxml-license = %{version}-%{release}
BuildRequires : buildreq-cmake
BuildRequires : qt6base-dev
BuildRequires : qt6declarative-dev
# Suppress stripping binaries
%define __strip /bin/true
%define debug_package %{nil}

%description
No detailed description available

%package dev
Summary: dev components for the qt6scxml package.
Group: Development
Requires: qt6scxml-lib = %{version}-%{release}
Provides: qt6scxml-devel = %{version}-%{release}
Requires: qt6scxml = %{version}-%{release}

%description dev
dev components for the qt6scxml package.


%package lib
Summary: lib components for the qt6scxml package.
Group: Libraries
Requires: qt6scxml-libexec = %{version}-%{release}
Requires: qt6scxml-license = %{version}-%{release}

%description lib
lib components for the qt6scxml package.


%package libexec
Summary: libexec components for the qt6scxml package.
Group: Default
Requires: qt6scxml-license = %{version}-%{release}

%description libexec
libexec components for the qt6scxml package.


%package license
Summary: license components for the qt6scxml package.
Group: Default

%description license
license components for the qt6scxml package.


%prep
%setup -q -n qtscxml-everywhere-src-6.8.2
cd %{_builddir}/qtscxml-everywhere-src-6.8.2
pushd ..
cp -a qtscxml-everywhere-src-6.8.2 buildavx2
popd

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1738707768
mkdir -p clr-build
pushd clr-build
export GCC_IGNORE_WERROR=1
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
CLEAR_INTERMEDIATE_CFLAGS="$CLEAR_INTERMEDIATE_CFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_FCFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_FFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_CXXFLAGS="$CLEAR_INTERMEDIATE_CXXFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CFLAGS="$CLEAR_INTERMEDIATE_CFLAGS"
CXXFLAGS="$CLEAR_INTERMEDIATE_CXXFLAGS"
FFLAGS="$CLEAR_INTERMEDIATE_FFLAGS"
FCFLAGS="$CLEAR_INTERMEDIATE_FCFLAGS"
ASFLAGS="$CLEAR_INTERMEDIATE_ASFLAGS"
LDFLAGS="$CLEAR_INTERMEDIATE_LDFLAGS"
export GOAMD64=v2
%cmake ..   -G 'Unix Makefiles'
make  %{?_smp_mflags}
popd
pushd ../buildavx2/
mkdir -p clr-build-avx2
pushd clr-build-avx2
export GCC_IGNORE_WERROR=1
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
CLEAR_INTERMEDIATE_CFLAGS="$CLEAR_INTERMEDIATE_CFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_FCFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_FFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_CXXFLAGS="$CLEAR_INTERMEDIATE_CXXFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CFLAGS="$CLEAR_INTERMEDIATE_CFLAGS"
CXXFLAGS="$CLEAR_INTERMEDIATE_CXXFLAGS"
FFLAGS="$CLEAR_INTERMEDIATE_FFLAGS"
FCFLAGS="$CLEAR_INTERMEDIATE_FCFLAGS"
ASFLAGS="$CLEAR_INTERMEDIATE_ASFLAGS"
LDFLAGS="$CLEAR_INTERMEDIATE_LDFLAGS"
GOAMD64=v3
CFLAGS="$CLEAR_INTERMEDIATE_CFLAGS -march=x86-64-v3 -Wl,-z,x86-64-v3 "
CXXFLAGS="$CLEAR_INTERMEDIATE_CXXFLAGS -march=x86-64-v3 -Wl,-z,x86-64-v3 "
FFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -march=x86-64-v3 -Wl,-z,x86-64-v3 "
FCFLAGS="$CLEAR_INTERMEDIATE_FCFLAGS -march=x86-64-v3 "
%cmake ..   -G 'Unix Makefiles'
make  %{?_smp_mflags}
popd
popd

%install
export GCC_IGNORE_WERROR=1
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
CLEAR_INTERMEDIATE_CFLAGS="$CLEAR_INTERMEDIATE_CFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_FCFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_FFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_CXXFLAGS="$CLEAR_INTERMEDIATE_CXXFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CFLAGS="$CLEAR_INTERMEDIATE_CFLAGS"
CXXFLAGS="$CLEAR_INTERMEDIATE_CXXFLAGS"
FFLAGS="$CLEAR_INTERMEDIATE_FFLAGS"
FCFLAGS="$CLEAR_INTERMEDIATE_FCFLAGS"
ASFLAGS="$CLEAR_INTERMEDIATE_ASFLAGS"
LDFLAGS="$CLEAR_INTERMEDIATE_LDFLAGS"
export SOURCE_DATE_EPOCH=1738707768
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/qt6scxml
cp %{_builddir}/qtscxml-everywhere-src-%{version}/LICENSES/Apache-2.0.txt %{buildroot}/usr/share/package-licenses/qt6scxml/1c619b057a9bf7a8234b3105fcfb5b375e749db1 || :
cp %{_builddir}/qtscxml-everywhere-src-%{version}/LICENSES/BSD-3-Clause.txt %{buildroot}/usr/share/package-licenses/qt6scxml/79453f55fa8ee32d7b95581473edcbfd043e088f || :
cp %{_builddir}/qtscxml-everywhere-src-%{version}/LICENSES/GPL-2.0-only.txt %{buildroot}/usr/share/package-licenses/qt6scxml/dc8f2e570bf431427dbc3bab9d4d551b53a60208 || :
cp %{_builddir}/qtscxml-everywhere-src-%{version}/LICENSES/GPL-3.0-only.txt %{buildroot}/usr/share/package-licenses/qt6scxml/7713a1753ce88f2c7e6b054ecc8e4c786df76300 || :
cp %{_builddir}/qtscxml-everywhere-src-%{version}/LICENSES/LGPL-3.0-only.txt %{buildroot}/usr/share/package-licenses/qt6scxml/c70af14df11e3908dfc10397b1ba4b1f346661f3 || :
cp %{_builddir}/qtscxml-everywhere-src-%{version}/tests/3rdparty/scion-tests/LICENSE.txt %{buildroot}/usr/share/package-licenses/qt6scxml/b314c7ebb7d599944981908b7f3ed33a30e78f3a || :
cp %{_builddir}/qtscxml-everywhere-src-%{version}/tests/3rdparty/scion-tests/scxml-test-framework/LICENSE.txt %{buildroot}/usr/share/package-licenses/qt6scxml/b314c7ebb7d599944981908b7f3ed33a30e78f3a || :
export GOAMD64=v2
pushd ../buildavx2/
GOAMD64=v3
pushd clr-build-avx2
%make_install_v3  || :
popd
popd
GOAMD64=v2
pushd clr-build
%make_install
popd
/usr/bin/elf-move.py avx2 %{buildroot}-v3 %{buildroot} %{buildroot}/usr/share/clear/filemap/filemap-%{name}

%files
%defattr(-,root,root,-)

%files dev
%defattr(-,root,root,-)
/usr/include/QtScxml/6.8.2/QtScxml/private/qscxmlcompiler_p.h
/usr/include/QtScxml/6.8.2/QtScxml/private/qscxmlcppdatamodel_p.h
/usr/include/QtScxml/6.8.2/QtScxml/private/qscxmldatamodel_p.h
/usr/include/QtScxml/6.8.2/QtScxml/private/qscxmldatamodelplugin_p.h
/usr/include/QtScxml/6.8.2/QtScxml/private/qscxmlevent_p.h
/usr/include/QtScxml/6.8.2/QtScxml/private/qscxmlexecutablecontent_p.h
/usr/include/QtScxml/6.8.2/QtScxml/private/qscxmlglobals_p.h
/usr/include/QtScxml/6.8.2/QtScxml/private/qscxmlinvokableservice_p.h
/usr/include/QtScxml/6.8.2/QtScxml/private/qscxmlstatemachine_p.h
/usr/include/QtScxml/6.8.2/QtScxml/private/qscxmlstatemachineinfo_p.h
/usr/include/QtScxml/6.8.2/QtScxml/private/qscxmltabledata_p.h
/usr/include/QtScxml/6.8.2/QtScxml/private/qtscxml-config_p.h
/usr/include/QtScxml/QScxmlCompiler
/usr/include/QtScxml/QScxmlCppDataModel
/usr/include/QtScxml/QScxmlDataModel
/usr/include/QtScxml/QScxmlDynamicScxmlServiceFactory
/usr/include/QtScxml/QScxmlError
/usr/include/QtScxml/QScxmlEvent
/usr/include/QtScxml/QScxmlInvokableService
/usr/include/QtScxml/QScxmlInvokableServiceFactory
/usr/include/QtScxml/QScxmlNullDataModel
/usr/include/QtScxml/QScxmlStateMachine
/usr/include/QtScxml/QScxmlStaticScxmlServiceFactory
/usr/include/QtScxml/QScxmlTableData
/usr/include/QtScxml/QtScxml
/usr/include/QtScxml/QtScxmlDepends
/usr/include/QtScxml/QtScxmlVersion
/usr/include/QtScxml/qscxmlcompiler.h
/usr/include/QtScxml/qscxmlcppdatamodel.h
/usr/include/QtScxml/qscxmldatamodel.h
/usr/include/QtScxml/qscxmlerror.h
/usr/include/QtScxml/qscxmlevent.h
/usr/include/QtScxml/qscxmlexecutablecontent.h
/usr/include/QtScxml/qscxmlglobals.h
/usr/include/QtScxml/qscxmlinvokableservice.h
/usr/include/QtScxml/qscxmlnulldatamodel.h
/usr/include/QtScxml/qscxmlstatemachine.h
/usr/include/QtScxml/qscxmltabledata.h
/usr/include/QtScxml/qtscxml-config.h
/usr/include/QtScxml/qtscxmlexports.h
/usr/include/QtScxml/qtscxmlversion.h
/usr/include/QtScxmlQml/6.8.2/QtScxmlQml/private/eventconnection_p.h
/usr/include/QtScxmlQml/6.8.2/QtScxmlQml/private/invokedservices_p.h
/usr/include/QtScxmlQml/6.8.2/QtScxmlQml/private/qscxmlqmlglobals_p.h
/usr/include/QtScxmlQml/6.8.2/QtScxmlQml/private/statemachineextended_p.h
/usr/include/QtScxmlQml/6.8.2/QtScxmlQml/private/statemachineloader_p.h
/usr/include/QtScxmlQml/QtScxmlQml
/usr/include/QtScxmlQml/QtScxmlQmlDepends
/usr/include/QtScxmlQml/QtScxmlQmlVersion
/usr/include/QtScxmlQml/qtscxmlqmlexports.h
/usr/include/QtScxmlQml/qtscxmlqmlversion.h
/usr/include/QtStateMachine/6.8.2/QtStateMachine/private/qabstractstate_p.h
/usr/include/QtStateMachine/6.8.2/QtStateMachine/private/qabstracttransition_p.h
/usr/include/QtStateMachine/6.8.2/QtStateMachine/private/qbasickeyeventtransition_p.h
/usr/include/QtStateMachine/6.8.2/QtStateMachine/private/qbasicmouseeventtransition_p.h
/usr/include/QtStateMachine/6.8.2/QtStateMachine/private/qeventtransition_p.h
/usr/include/QtStateMachine/6.8.2/QtStateMachine/private/qfinalstate_p.h
/usr/include/QtStateMachine/6.8.2/QtStateMachine/private/qhistorystate_p.h
/usr/include/QtStateMachine/6.8.2/QtStateMachine/private/qsignaleventgenerator_p.h
/usr/include/QtStateMachine/6.8.2/QtStateMachine/private/qsignaltransition_p.h
/usr/include/QtStateMachine/6.8.2/QtStateMachine/private/qstate_p.h
/usr/include/QtStateMachine/6.8.2/QtStateMachine/private/qstatemachine_p.h
/usr/include/QtStateMachine/6.8.2/QtStateMachine/private/qtstatemachine-config_p.h
/usr/include/QtStateMachine/QAbstractState
/usr/include/QtStateMachine/QAbstractTransition
/usr/include/QtStateMachine/QEventTransition
/usr/include/QtStateMachine/QFinalState
/usr/include/QtStateMachine/QHistoryState
/usr/include/QtStateMachine/QKeyEventTransition
/usr/include/QtStateMachine/QMouseEventTransition
/usr/include/QtStateMachine/QSignalTransition
/usr/include/QtStateMachine/QState
/usr/include/QtStateMachine/QStateMachine
/usr/include/QtStateMachine/QtStateMachine
/usr/include/QtStateMachine/QtStateMachineDepends
/usr/include/QtStateMachine/QtStateMachineVersion
/usr/include/QtStateMachine/qabstractstate.h
/usr/include/QtStateMachine/qabstracttransition.h
/usr/include/QtStateMachine/qeventtransition.h
/usr/include/QtStateMachine/qfinalstate.h
/usr/include/QtStateMachine/qhistorystate.h
/usr/include/QtStateMachine/qkeyeventtransition.h
/usr/include/QtStateMachine/qmouseeventtransition.h
/usr/include/QtStateMachine/qsignaltransition.h
/usr/include/QtStateMachine/qstate.h
/usr/include/QtStateMachine/qstatemachine.h
/usr/include/QtStateMachine/qstatemachineglobal.h
/usr/include/QtStateMachine/qtstatemachine-config.h
/usr/include/QtStateMachine/qtstatemachineexports.h
/usr/include/QtStateMachine/qtstatemachineversion.h
/usr/include/QtStateMachineQml/6.8.2/QtStateMachineQml/private/childrenprivate_p.h
/usr/include/QtStateMachineQml/6.8.2/QtStateMachineQml/private/finalstate_p.h
/usr/include/QtStateMachineQml/6.8.2/QtStateMachineQml/private/qstatemachineqmlglobals_p.h
/usr/include/QtStateMachineQml/6.8.2/QtStateMachineQml/private/signaltransition_p.h
/usr/include/QtStateMachineQml/6.8.2/QtStateMachineQml/private/state_p.h
/usr/include/QtStateMachineQml/6.8.2/QtStateMachineQml/private/statemachine_p.h
/usr/include/QtStateMachineQml/6.8.2/QtStateMachineQml/private/statemachineforeign_p.h
/usr/include/QtStateMachineQml/6.8.2/QtStateMachineQml/private/timeouttransition_p.h
/usr/include/QtStateMachineQml/QtStateMachineQml
/usr/include/QtStateMachineQml/QtStateMachineQmlDepends
/usr/include/QtStateMachineQml/QtStateMachineQmlVersion
/usr/include/QtStateMachineQml/qtstatemachineqmlexports.h
/usr/include/QtStateMachineQml/qtstatemachineqmlversion.h
/usr/lib64/cmake/Qt6BuildInternals/StandaloneTests/QtScxmlTestsConfig.cmake
/usr/lib64/cmake/Qt6Qml/QmlPlugins/Qt6declarative_scxmlAdditionalTargetInfo.cmake
/usr/lib64/cmake/Qt6Qml/QmlPlugins/Qt6declarative_scxmlConfig.cmake
/usr/lib64/cmake/Qt6Qml/QmlPlugins/Qt6declarative_scxmlConfigVersion.cmake
/usr/lib64/cmake/Qt6Qml/QmlPlugins/Qt6declarative_scxmlConfigVersionImpl.cmake
/usr/lib64/cmake/Qt6Qml/QmlPlugins/Qt6declarative_scxmlTargets-relwithdebinfo.cmake
/usr/lib64/cmake/Qt6Qml/QmlPlugins/Qt6declarative_scxmlTargets.cmake
/usr/lib64/cmake/Qt6Qml/QmlPlugins/Qt6qtqmlstatemachineAdditionalTargetInfo.cmake
/usr/lib64/cmake/Qt6Qml/QmlPlugins/Qt6qtqmlstatemachineConfig.cmake
/usr/lib64/cmake/Qt6Qml/QmlPlugins/Qt6qtqmlstatemachineConfigVersion.cmake
/usr/lib64/cmake/Qt6Qml/QmlPlugins/Qt6qtqmlstatemachineConfigVersionImpl.cmake
/usr/lib64/cmake/Qt6Qml/QmlPlugins/Qt6qtqmlstatemachineTargets-relwithdebinfo.cmake
/usr/lib64/cmake/Qt6Qml/QmlPlugins/Qt6qtqmlstatemachineTargets.cmake
/usr/lib64/cmake/Qt6Scxml/Qt6QScxmlEcmaScriptDataModelPluginAdditionalTargetInfo.cmake
/usr/lib64/cmake/Qt6Scxml/Qt6QScxmlEcmaScriptDataModelPluginConfig.cmake
/usr/lib64/cmake/Qt6Scxml/Qt6QScxmlEcmaScriptDataModelPluginConfigVersion.cmake
/usr/lib64/cmake/Qt6Scxml/Qt6QScxmlEcmaScriptDataModelPluginConfigVersionImpl.cmake
/usr/lib64/cmake/Qt6Scxml/Qt6QScxmlEcmaScriptDataModelPluginTargets-relwithdebinfo.cmake
/usr/lib64/cmake/Qt6Scxml/Qt6QScxmlEcmaScriptDataModelPluginTargets.cmake
/usr/lib64/cmake/Qt6Scxml/Qt6ScxmlAdditionalTargetInfo.cmake
/usr/lib64/cmake/Qt6Scxml/Qt6ScxmlConfig.cmake
/usr/lib64/cmake/Qt6Scxml/Qt6ScxmlConfigVersion.cmake
/usr/lib64/cmake/Qt6Scxml/Qt6ScxmlConfigVersionImpl.cmake
/usr/lib64/cmake/Qt6Scxml/Qt6ScxmlDependencies.cmake
/usr/lib64/cmake/Qt6Scxml/Qt6ScxmlMacros.cmake
/usr/lib64/cmake/Qt6Scxml/Qt6ScxmlPlugins.cmake
/usr/lib64/cmake/Qt6Scxml/Qt6ScxmlTargets-relwithdebinfo.cmake
/usr/lib64/cmake/Qt6Scxml/Qt6ScxmlTargets.cmake
/usr/lib64/cmake/Qt6Scxml/Qt6ScxmlVersionlessAliasTargets.cmake
/usr/lib64/cmake/Qt6Scxml/Qt6ScxmlVersionlessTargets.cmake
/usr/lib64/cmake/Qt6ScxmlQml/Qt6ScxmlQmlAdditionalTargetInfo.cmake
/usr/lib64/cmake/Qt6ScxmlQml/Qt6ScxmlQmlConfig.cmake
/usr/lib64/cmake/Qt6ScxmlQml/Qt6ScxmlQmlConfigVersion.cmake
/usr/lib64/cmake/Qt6ScxmlQml/Qt6ScxmlQmlConfigVersionImpl.cmake
/usr/lib64/cmake/Qt6ScxmlQml/Qt6ScxmlQmlDependencies.cmake
/usr/lib64/cmake/Qt6ScxmlQml/Qt6ScxmlQmlTargets-relwithdebinfo.cmake
/usr/lib64/cmake/Qt6ScxmlQml/Qt6ScxmlQmlTargets.cmake
/usr/lib64/cmake/Qt6ScxmlQml/Qt6ScxmlQmlVersionlessAliasTargets.cmake
/usr/lib64/cmake/Qt6ScxmlQml/Qt6ScxmlQmlVersionlessTargets.cmake
/usr/lib64/cmake/Qt6ScxmlTools/Qt6ScxmlToolsAdditionalTargetInfo.cmake
/usr/lib64/cmake/Qt6ScxmlTools/Qt6ScxmlToolsConfig.cmake
/usr/lib64/cmake/Qt6ScxmlTools/Qt6ScxmlToolsConfigVersion.cmake
/usr/lib64/cmake/Qt6ScxmlTools/Qt6ScxmlToolsConfigVersionImpl.cmake
/usr/lib64/cmake/Qt6ScxmlTools/Qt6ScxmlToolsDependencies.cmake
/usr/lib64/cmake/Qt6ScxmlTools/Qt6ScxmlToolsTargets-relwithdebinfo.cmake
/usr/lib64/cmake/Qt6ScxmlTools/Qt6ScxmlToolsTargets.cmake
/usr/lib64/cmake/Qt6ScxmlTools/Qt6ScxmlToolsVersionlessTargets.cmake
/usr/lib64/cmake/Qt6StateMachine/Qt6StateMachineAdditionalTargetInfo.cmake
/usr/lib64/cmake/Qt6StateMachine/Qt6StateMachineConfig.cmake
/usr/lib64/cmake/Qt6StateMachine/Qt6StateMachineConfigVersion.cmake
/usr/lib64/cmake/Qt6StateMachine/Qt6StateMachineConfigVersionImpl.cmake
/usr/lib64/cmake/Qt6StateMachine/Qt6StateMachineDependencies.cmake
/usr/lib64/cmake/Qt6StateMachine/Qt6StateMachineTargets-relwithdebinfo.cmake
/usr/lib64/cmake/Qt6StateMachine/Qt6StateMachineTargets.cmake
/usr/lib64/cmake/Qt6StateMachine/Qt6StateMachineVersionlessAliasTargets.cmake
/usr/lib64/cmake/Qt6StateMachine/Qt6StateMachineVersionlessTargets.cmake
/usr/lib64/cmake/Qt6StateMachineQml/Qt6StateMachineQmlAdditionalTargetInfo.cmake
/usr/lib64/cmake/Qt6StateMachineQml/Qt6StateMachineQmlConfig.cmake
/usr/lib64/cmake/Qt6StateMachineQml/Qt6StateMachineQmlConfigVersion.cmake
/usr/lib64/cmake/Qt6StateMachineQml/Qt6StateMachineQmlConfigVersionImpl.cmake
/usr/lib64/cmake/Qt6StateMachineQml/Qt6StateMachineQmlDependencies.cmake
/usr/lib64/cmake/Qt6StateMachineQml/Qt6StateMachineQmlTargets-relwithdebinfo.cmake
/usr/lib64/cmake/Qt6StateMachineQml/Qt6StateMachineQmlTargets.cmake
/usr/lib64/cmake/Qt6StateMachineQml/Qt6StateMachineQmlVersionlessAliasTargets.cmake
/usr/lib64/cmake/Qt6StateMachineQml/Qt6StateMachineQmlVersionlessTargets.cmake
/usr/lib64/libQt6Scxml.prl
/usr/lib64/libQt6Scxml.so
/usr/lib64/libQt6ScxmlQml.prl
/usr/lib64/libQt6ScxmlQml.so
/usr/lib64/libQt6StateMachine.prl
/usr/lib64/libQt6StateMachine.so
/usr/lib64/libQt6StateMachineQml.prl
/usr/lib64/libQt6StateMachineQml.so
/usr/lib64/pkgconfig/Qt6Scxml.pc
/usr/lib64/pkgconfig/Qt6ScxmlQml.pc
/usr/lib64/pkgconfig/Qt6StateMachine.pc
/usr/lib64/pkgconfig/Qt6StateMachineQml.pc
/usr/lib64/qt6/mkspecs/features/qscxmlc.prf
/usr/lib64/qt6/mkspecs/modules/qt_lib_scxml.pri
/usr/lib64/qt6/mkspecs/modules/qt_lib_scxml_private.pri
/usr/lib64/qt6/mkspecs/modules/qt_lib_scxmlqml.pri
/usr/lib64/qt6/mkspecs/modules/qt_lib_scxmlqml_private.pri
/usr/lib64/qt6/mkspecs/modules/qt_lib_statemachine.pri
/usr/lib64/qt6/mkspecs/modules/qt_lib_statemachine_private.pri
/usr/lib64/qt6/mkspecs/modules/qt_lib_statemachineqml.pri
/usr/lib64/qt6/mkspecs/modules/qt_lib_statemachineqml_private.pri

%files lib
%defattr(-,root,root,-)
/V3/usr/lib64/libQt6Scxml.so.6.8.2
/V3/usr/lib64/libQt6ScxmlQml.so.6.8.2
/V3/usr/lib64/libQt6StateMachine.so.6.8.2
/V3/usr/lib64/libQt6StateMachineQml.so.6.8.2
/V3/usr/lib64/qt6/plugins/scxmldatamodel/libqscxmlecmascriptdatamodel.so
/V3/usr/lib64/qt6/qml/QtQml/StateMachine/libqtqmlstatemachineplugin.so
/V3/usr/lib64/qt6/qml/QtScxml/libdeclarative_scxmlplugin.so
/usr/lib64/libQt6Scxml.so.6
/usr/lib64/libQt6Scxml.so.6.8.2
/usr/lib64/libQt6ScxmlQml.so.6
/usr/lib64/libQt6ScxmlQml.so.6.8.2
/usr/lib64/libQt6StateMachine.so.6
/usr/lib64/libQt6StateMachine.so.6.8.2
/usr/lib64/libQt6StateMachineQml.so.6
/usr/lib64/libQt6StateMachineQml.so.6.8.2
/usr/lib64/qt6/metatypes/qt6scxml_relwithdebinfo_metatypes.json
/usr/lib64/qt6/metatypes/qt6scxmlqml_relwithdebinfo_metatypes.json
/usr/lib64/qt6/metatypes/qt6statemachine_relwithdebinfo_metatypes.json
/usr/lib64/qt6/metatypes/qt6statemachineqml_relwithdebinfo_metatypes.json
/usr/lib64/qt6/modules/Scxml.json
/usr/lib64/qt6/modules/ScxmlQml.json
/usr/lib64/qt6/modules/StateMachine.json
/usr/lib64/qt6/modules/StateMachineQml.json
/usr/lib64/qt6/plugins/scxmldatamodel/libqscxmlecmascriptdatamodel.so
/usr/lib64/qt6/qml/QtQml/StateMachine/libqtqmlstatemachineplugin.so
/usr/lib64/qt6/qml/QtQml/StateMachine/plugins.qmltypes
/usr/lib64/qt6/qml/QtQml/StateMachine/qmldir
/usr/lib64/qt6/qml/QtScxml/libdeclarative_scxmlplugin.so
/usr/lib64/qt6/qml/QtScxml/plugins.qmltypes
/usr/lib64/qt6/qml/QtScxml/qmldir
/usr/lib64/qt6/sbom/qtscxml-6.8.2.spdx

%files libexec
%defattr(-,root,root,-)
/V3/usr/libexec/qscxmlc
/usr/libexec/qscxmlc

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/qt6scxml/1c619b057a9bf7a8234b3105fcfb5b375e749db1
/usr/share/package-licenses/qt6scxml/7713a1753ce88f2c7e6b054ecc8e4c786df76300
/usr/share/package-licenses/qt6scxml/79453f55fa8ee32d7b95581473edcbfd043e088f
/usr/share/package-licenses/qt6scxml/b314c7ebb7d599944981908b7f3ed33a30e78f3a
/usr/share/package-licenses/qt6scxml/c70af14df11e3908dfc10397b1ba4b1f346661f3
/usr/share/package-licenses/qt6scxml/dc8f2e570bf431427dbc3bab9d4d551b53a60208
