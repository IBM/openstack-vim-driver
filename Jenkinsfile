#!/usr/bin/env groovy

String tarquinBranch = "develop"

library "tarquin@$tarquinBranch"

pipelinePy {
  pkgInfoPath = 'osvimdriver/pkg_info.json'
  applicationName = 'os-vim-driver'
  releaseArtifactsPath = 'release-artifacts'
  attachDocsToRelease = true
  attachHelmToRelease = true
}
