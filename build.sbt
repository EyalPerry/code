ThisBuild / scalaVersion := "2.13.16"

ThisBuild / version := "0.1.0"

ThisBuild / organization := "com.example"

lazy val root = (project in file("."))
  .settings(
    name := "data-eng-template",

    // Add dependencies here
    libraryDependencies ++= Seq(
      "org.apache.spark" %% "spark-sql" % "3.5.0",
      // Add more like Delta, Kafka if needed
    )
  )
