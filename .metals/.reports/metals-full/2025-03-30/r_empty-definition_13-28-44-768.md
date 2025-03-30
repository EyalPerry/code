error id: 
file://<WORKSPACE>/build.sbt
empty definition using pc, found symbol in pc: 
empty definition using semanticdb
empty definition using fallback
non-local guesses:

offset: 179
uri: file://<WORKSPACE>/build.sbt
text:
```scala
ThisBuild / scalaVersion := "2.13.16"

ThisBuild / version := "0.1.0"

ThisBuild / organization := "com.example"

lazy val root = (project in file("."))
  .settings(
    name := "@@data-eng-template",

    // Add dependencies here
    libraryDependencies ++= Seq(
      "org.apache.spark" %% "spark-sql" % "3.5.0"
      // Add more like Delta, Kafka if needed
    )
  )

```


#### Short summary: 

empty definition using pc, found symbol in pc: 