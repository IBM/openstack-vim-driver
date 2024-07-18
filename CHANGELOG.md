# Change Log

## [3.5.2](https://github.com/IBM/openstack-vim-driver/tree/3.5.2) (2024-07-18)
[Full Changelog](https://github.com/IBM/openstack-vim-driver/compare/3.5.1...3.5.2)

**Implemented enhancements:**
- Update Ignition to 3.6.3 to fix the issue of request transfer-encoding with chunked format

## [3.5.1](https://github.com/IBM/openstack-vim-driver/tree/3.5.1) (2024-06-18)
[Full Changelog](https://github.com/IBM/openstack-vim-driver/compare/3.5.0...3.5.1)

**Implemented enhancements:**
- Update ignition version to 3.6.2 to fix for CP4NA UI driver log messages issue with ansible-lifecycle-driver

## [3.5.0](https://github.com/IBM/openstack-vim-driver/tree/3.5.0) (2024-05-29)
[Full Changelog](https://github.com/IBM/openstack-vim-driver/compare/3.4.0...3.5.0)

**Implemented enhancements:**
- Update ignition version to 3.6.1 [\#156](https://github.com/IBM/openstack-vim-driver/issues/156)
- Fix Security Vulnerabilites  [\#154](https://github.com/IBM/openstack-vim-driver/issues/154)

## [3.4.0](https://github.com/IBM/openstack-vim-driver/tree/3.4.0) (2023-09-20)
[Full Changelog](https://github.com/IBM/openstack-vim-driver/compare/3.3.0...3.4.0)

**Implemented enhancements:**
- os-vim-driver Stack status 'SNAPSHOT_COMPLETE' is not an adoptable state [\#114](https://github.com/IBM/openstack-vim-driver/issues/114)
- Fix for Bug #128 does not validate for str only data for masking  [\#142](https://github.com/IBM/openstack-vim-driver/issues/142)

**Dependencies:**
- Update Ignition with latest version 3.5.2 [\#144](https://github.com/IBM/openstack-vim-driver/issues/144)


## [3.3.0](https://github.com/IBM/openstack-vim-driver/tree/3.3.0) (2023-06-06)
[Full Changelog](https://github.com/IBM/openstack-vim-driver/compare/3.2.1...3.3.0)

**Implemented enhancements:**
- Assembly Instance creation failed in openstack vim driver with 3.3.0-rc1 pre-release image [\#134](https://github.com/IBM/openstack-vim-driver/issues/134)
- Build issue in openstack-vim-driver with 'rc' tag [\#130](https://github.com/IBM/openstack-vim-driver/issues/130)
- Mask password in Openstack VIM driver logs [\#128](https://github.com/IBM/openstack-vim-driver/issues/128)
- Enable Logging for External Request & Response [\#122](https://github.com/IBM/openstack-vim-driver/issues/122)

**Dependencies:**
- Update Ignition to latest version 3.5.1 [\#126](https://github.com/IBM/openstack-vim-driver/issues/126)

## [3.2.1](https://github.com/IBM/openstack-vim-driver/tree/3.2.1) (2022-12-08)
[Full Changelog](https://github.com/IBM/openstack-vim-driver/compare/3.2.0...3.2.1)

**Implemented enhancements:**
- Fix Vulnerabilities [\#116](https://github.com/IBM/openstack-vim-driver/issues/116)
- Update Documentation [\#112](https://github.com/IBM/openstack-vim-driver/issues/112)

**Dependencies:**
- Upgraded to Ignition 3.4.2 [\#117](https://github.com/IBM/openstack-vim-driver/issues/117)


## [3.2.0](https://github.com/IBM/openstack-vim-driver/tree/3.2.0) (2022-09-30)
[Full Changelog](https://github.com/IBM/openstack-vim-driver/compare/3.1.1...3.2.0)

**Dependencies:**
- Upgraded to Ignition 3.4.1,  which includes Multitenency [\#106](https://github.com/IBM/openstack-vim-driver/issues/106)

**Implemented enhancements:**
- Add note for KAFKA address change  [\#97](https://github.com/IBM/openstack-vim-driver/issues/97)
- Update install instructions for Openstack VIM Driver [\#99](https://github.com/IBM/openstack-vim-driver/issues/99)
- Fix Vulnerabilities [\#103](https://github.com/IBM/openstack-vim-driver/issues/103)

## [3.1.1](https://github.com/IBM/openstack-vim-driver/tree/3.1.1) (2022-05-31)
[Full Changelog](https://github.com/IBM/openstack-vim-driver/compare/3.1.0...3.1.1)

**Implemented enhancements:**
- Ingress removal [\#88](https://github.com/IBM/openstack-vim-driver/issues/88)
- Kafka instance name changed & updated ignition version [\#91](https://github.com/IBM/openstack-vim-driver/issues/91)

## [3.1.0](https://github.com/IBM/openstack-vim-driver/tree/3.1.0) (2021-12-10)
[Full Changelog](https://github.com/IBM/openstack-vim-driver/compare/3.0.1...3.1.0)

**Implemented enhancements:**
- Remove uwsgi and support graceful shutdown [\#85](https://github.com/IBM/openstack-vim-driver/issues/85)

## [3.0.1](https://github.com/IBM/openstack-vim-driver/tree/3.0.1) (2021-07-16)
[Full Changelog](https://github.com/IBM/openstack-vim-driver/compare/3.0.0...3.0.1)

**Implemented enhancements:**
- Uplift dependency versions [\#81](https://github.com/IBM/openstack-vim-driver/issues/81)

## [3.0.0](https://github.com/IBM/openstack-vim-driver/tree/3.0.0) (2021-04-29)
[Full Changelog](https://github.com/IBM/openstack-vim-driver/compare/2.1.0...3.0.0)

**Implemented enhancements:**
- Support structured properties [\#76](https://github.com/IBM/openstack-vim-driver/issues/76)
- Update connection_address to iaf-system-kafka-bootstrap:9092 in driver values.yaml to be compatible with TNC-O installed with IAF  [\#78](https://github.com/IBM/openstack-vim-driver/issues/78)

## [2.1.0](https://github.com/accanto-systems/openstack-vim-driver/tree/2.1.0) (2020-09-30)
[Full Changelog](https://github.com/accanto-systems/openstack-vim-driver/compare/2.0.1...2.1.0)

**Implemented enhancements:**
- Add Support for Adopt Lifecycle Transitions [\#68](https://github.com/accanto-systems/openstack-vim-driver/issues/68)
- Helm installation does not work for OCP 4.4 (Kubernetes 1.17) [\#62](https://github.com/accanto-systems/openstack-vim-driver/issues/62)
- Driver will not run in OCP Restricted SCC [\#61](https://github.com/accanto-systems/openstack-vim-driver/issues/61)
- Issue/56 - support imported heat and tosca files [\#60](https://github.com/accanto-systems/openstack-vim-driver/issues/60)
- Support imported files in Heat [\#56](https://github.com/accanto-systems/openstack-vim-driver/issues/56)
- Support NFV tosca types [\#51](https://github.com/accanto-systems/openstack-vim-driver/issues/51)

**Fixed bugs:**

**Documentation:**

## [2.0.1](https://github.com/accanto-systems/openstack-vim-driver/tree/2.0.1) (2020-06-09)
[Full Changelog](https://github.com/accanto-systems/openstack-vim-driver/compare/2.0.0...2.0.1)

**Implemented enhancements:**
- Increase default number of processes [\#53](https://github.com/accanto-systems/openstack-vim-driver/issues/53)

**Fixed bugs:**
- NoBrokersAvailable exceptions during Kafka sends and receives [\#57](https://github.com/accanto-systems/openstack-vim-driver/issues/57)

**Documentation:**
- Docs: Deployment Location - Use of string, e.g. os_cacert in deployment location invalid [\#52](https://github.com/accanto-systems/openstack-vim-driver/issues/52)

## [2.0.0](https://github.com/accanto-systems/openstack-vim-driver/tree/2.0.0) (2020-05-19)
[Full Changelog](https://github.com/accanto-systems/openstack-vim-driver/compare/1.0.0...2.0.0)

**Implemented enhancements:**
- Support openstack certificates [\#43](https://github.com/accanto-systems/openstack-vim-driver/issues/43)
- Update API handling to support new Resource Driver API [\#49](https://github.com/accanto-systems/openstack-vim-driver/issues/49)

**Fixed bugs:**
- Log level causing high disk usage [\#44](https://github.com/accanto-systems/openstack-vim-driver/issues/44)

**Depdendencies:**
- Upgraded to Ignition version 2.0.0

## [1.0.0](https://github.com/accanto-systems/openstack-vim-driver/tree/1.0.0) (2020-02-20)
[Full Changelog](https://github.com/accanto-systems/openstack-vim-driver/compare/0.7.1...1.0.0)

**Implemented enhancements:**

- Allow key properties to be used as inputs to Heat templates [\#39](https://github.com/accanto-systems/openstack-vim-driver/issues/39)

**Documentation:**
- Deployment Location properties format [\#35](https://github.com/accanto-systems/openstack-vim-driver/issues/35)
- Ensure documentation correct for 1.0.0 [\#38](https://github.com/accanto-systems/openstack-vim-driver/issues/38)

**Depdendencies:**
- Upgraded to Ignition version 1.0.0

## [0.7.1](https://github.com/accanto-systems/openstack-vim-driver/tree/0.7.1) (2020-02-17)
[Full Changelog](https://github.com/accanto-systems/openstack-vim-driver/compare/0.7.0...0.7.1)

**Fixed bugs:**

- Delete Infrastructure on a Stack that does not exists fails with internal server error [\#36](https://github.com/accanto-systems/openstack-vim-driver/issues/36)

## [0.7.0](https://github.com/accanto-systems/openstack-vim-driver/tree/0.7.0) (2020-01-30)
[Full Changelog](https://github.com/accanto-systems/openstack-vim-driver/compare/0.6.0...0.7.0)

**Implemented enhancements:**

- Add liveness and readiness probe to helm chart [\#33](https://github.com/accanto-systems/openstack-vim-driver/issues/33)
- Add SSL support [\#31](https://github.com/accanto-systems/openstack-vim-driver/issues/31)
- Autoscaling on CPU usage [\#29](https://github.com/accanto-systems/openstack-vim-driver/issues/29)

**Dependencies:**

- Upgraded to Ignition 0.8.0

## [0.6.0](https://github.com/accanto-systems/openstack-vim-driver/tree/0.6.0) (2020-01-13)
[Full Changelog](https://github.com/accanto-systems/openstack-vim-driver/compare/0.5.0...0.6.0)

**Implemented enhancements:**

- Update InfrastructureDriver to accept and make use of systemProperties [\#27](https://github.com/accanto-systems/openstack-vim-driver/issues/27)

**Maintenaince Tasks:**

- As part of [\#27](https://github.com/accanto-systems/openstack-vim-driver/issues/27), the Ignition version used by this driver has been updated to v0.7.0

## [0.5.0](https://github.com/accanto-systems/openstack-vim-driver/tree/0.5.0) (2019-12-13)
[Full Changelog](https://github.com/accanto-systems/openstack-vim-driver/compare/0.4.2...0.5.0)

**Maintenaince Tasks:**

- Upgrade ignition framework version to 0.6.2 [\#25](https://github.com/accanto-systems/openstack-vim-driver/issues/25)

## [0.4.2](https://github.com/accanto-systems/openstack-vim-driver/tree/0.4.2) (2019-12-09)
[Full Changelog](https://github.com/accanto-systems/openstack-vim-driver/compare/0.4.1...0.4.2)

**Fixed bugs:**

- Assume stack_id of "0" is the same as no stack_id

## [0.4.1](https://github.com/accanto-systems/openstack-vim-driver/tree/0.4.1) (2019-12-05)
[Full Changelog](https://github.com/accanto-systems/openstack-vim-driver/compare/0.4.0...0.4.1)

**Fixed bugs:**

- Check if stack_id is not None [\#24](https://github.com/accanto-systems/openstack-vim-driver/issues/24)

## [0.4.0](https://github.com/accanto-systems/openstack-vim-driver/tree/0.4.0) (2019-12-05)
[Full Changelog](https://github.com/accanto-systems/openstack-vim-driver/compare/0.3.0...0.4.0)

**Fixed bugs:**

- OSError('libc not found') when running with Guincorn [\#21](https://github.com/accanto-systems/openstack-vim-driver/issues/21)

**Implemented enhancements:**

- Recognise existing stacks on request [\#23](https://github.com/accanto-systems/openstack-vim-driver/issues/23)

**Maintenaince Tasks:**

- Tighten restrictions on dependency versions [\#18](https://github.com/accanto-systems/openstack-vim-driver/issues/18)
- Support building Docker image with development version of Ignition [\#19](https://github.com/accanto-systems/openstack-vim-driver/issues/19)

**Documentation:**

- Improve documentation layout and include descriptions of property handling [\#15](https://github.com/accanto-systems/openstack-vim-driver/issues/15)

## [0.3.0](https://github.com/accanto-systems/openstack-vim-driver/tree/0.3.0) (2019-10-09)
[Full Changelog](https://github.com/accanto-systems/openstack-vim-driver/compare/0.2.0...0.3.0)

**Dependencies:**

- Upgraded to Ignition 0.4.0

**Fixed bugs:**

- Configure helm chart to explicitly run the container as "old" user [\#9](https://github.com/accanto-systems/openstack-vim-driver/issues/9)

**Implemented enhancements:**

- Add affinity and toleration rules to helm chart [\#13](https://github.com/accanto-systems/openstack-vim-driver/issues/13)
- Configure K8s Label to enable Filebeat logging [\#11](https://github.com/accanto-systems/openstack-vim-driver/issues/11)
- Support Heat templates [\#7](https://github.com/accanto-systems/openstack-vim-driver/issues/7)
- Include resource requests and limits configuration in Helm chart [\#5](https://github.com/accanto-systems/openstack-vim-driver/issues/5)

## [0.2.0](https://github.com/accanto-systems/openstack-vim-driver/tree/0.2.0) (2019-09-18)
[Full Changelog](https://github.com/accanto-systems/openstack-vim-driver/compare/0.1.0...0.2.0)

**Fixed bugs:**

- Query infrastructure task does not return 4xx status code when not found [\#1](https://github.com/accanto-systems/openstack-vim-driver/issues/1)

**Closed issues:**

- Upgrade Ignition framework version to 0.2.0 [\#3](https://github.com/accanto-systems/openstack-vim-driver/issues/3)

**Merged pull requests:**

- Resolves \#3 by upgrading the Ignition version to 0.2.0 [\#4](https://github.com/accanto-systems/openstack-vim-driver/pull/4) ([dvaccarosenna](https://github.com/dvaccarosenna))
- issue1 - get infrastructure API to return a 400 when the stack cannot… [\#2](https://github.com/accanto-systems/openstack-vim-driver/pull/2) ([dvaccarosenna](https://github.com/dvaccarosenna))

## [0.1.0](https://github.com/accanto-systems/openstack-vim-driver/tree/0.1.0) (2019-09-02)


\* *This Change Log was automatically generated by [github_changelog_generator](https://github.com/skywinder/Github-Changelog-Generator)*
