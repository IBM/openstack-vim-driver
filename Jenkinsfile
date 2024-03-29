#!/usr/bin/env groovy

String tarquinBranch = "CPNA-1189"

library "tarquin@$tarquinBranch"

pipelinePy {
  pkgInfoPath = 'osvimdriver/pkg_info.json'
  applicationName = 'os-vim-driver'
  releaseArtifactsPath = 'release-artifacts'
  attachDocsToRelease = true
  attachHelmToRelease = true
}
